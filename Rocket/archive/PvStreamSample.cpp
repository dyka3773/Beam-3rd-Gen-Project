// *****************************************************************************
//
//      Copyright (c) 2013, Pleora Technologies Inc., All rights reserved.
//
// *****************************************************************************

//
// Shows how to use a PvStream object to acquire images from a GigE Vision or
// USB3 Vision device.
//

#include <PvSampleUtils.h>
#include <PvDevice.h>
#include <PvDeviceGEV.h>
#include <PvDeviceU3V.h>
#include <PvStream.h>
#include <PvStreamGEV.h>
#include <PvStreamU3V.h>
#include <PvBuffer.h>
#include "Mp4WriterWin32.h"

#include <list>
typedef std::list<PvBuffer *> BufferList;
class ImageSaving;
PV_INIT_SIGNAL_HANDLER();

#define BUFFER_COUNT ( 16 )

///
/// Function Prototypes
///
PvDevice *ConnectToDevice( const PvString &aConnectionID );
PvStream *OpenStream( const PvString &aConnectionID );
void ConfigureStream( PvDevice *aDevice, PvStream *aStream );
void CreateStreamBuffers( PvDevice *aDevice, PvStream *aStream, BufferList *aBufferList );
void AcquireImages( PvDevice *aDevice, PvStream *aStream );
void FreeStreamBuffers( BufferList *aBufferList );
PvMp4Writer mp4test;
uint32_t lFileSizeDelta = 0;

//
// Main function
//
int main()
{
    PvDevice *lDevice = NULL;
    PvStream *lStream = NULL;
    BufferList lBufferList;

    PV_SAMPLE_INIT();


    mp4test.SetAvgBitrate( 2000000 );


    cout << "PvStreamSample:" << endl << endl;

    PvString lConnectionID;
    if ( PvSelectDevice( &lConnectionID ) )
    {
        lDevice = ConnectToDevice( lConnectionID );
        if ( NULL != lDevice )
        {
            lStream = OpenStream( lConnectionID );
            if ( NULL != lStream )
            {
                ConfigureStream( lDevice, lStream );
                CreateStreamBuffers( lDevice, lStream, &lBufferList );
                AcquireImages( lDevice, lStream );
                FreeStreamBuffers( &lBufferList );
                
                // Close the stream
                cout << "Closing stream" << endl;
                lStream->Close();
                PvStream::Free( lStream );    
            }

            // Disconnect the device
            cout << "Disconnecting device" << endl;
            lDevice->Disconnect();
            PvDevice::Free( lDevice );
        }
    }

    cout << endl;
    cout << "<press a key to exit>" << endl;
    PvWaitForKeyPress();

    PV_SAMPLE_TERMINATE();

    return 0;
}

PvDevice *ConnectToDevice( const PvString &aConnectionID )
{
    PvDevice *lDevice;
    PvResult lResult;

    // Connect to the GigE Vision or USB3 Vision device
    cout << "Connecting to device." << endl;
    lDevice = PvDevice::CreateAndConnect( aConnectionID, &lResult );
    if ( lDevice == NULL )
    {
        cout << "Unable to connect to device: "
        << lResult.GetCodeString().GetAscii()
        << " ("
        << lResult.GetDescription().GetAscii()
        << ")" << endl;
    }

 
    return lDevice;
}

PvStream *OpenStream( const PvString &aConnectionID )
{
    PvStream *lStream;
    PvResult lResult;

    // Open stream to the GigE Vision or USB3 Vision device
    cout << "Opening stream from device." << endl;
    lStream = PvStream::CreateAndOpen( aConnectionID, &lResult );
    if ( lStream == NULL )
    {
        cout << "Unable to stream from device. "
            << lResult.GetCodeString().GetAscii()
            << " ("
            << lResult.GetDescription().GetAscii()
            << ")"
            << endl;
    }

    return lStream;
}

void ConfigureStream( PvDevice *aDevice, PvStream *aStream )
{
    // If this is a GigE Vision device, configure GigE Vision specific streaming parameters
    PvDeviceGEV* lDeviceGEV = dynamic_cast<PvDeviceGEV *>( aDevice );
    if ( lDeviceGEV != NULL )
    {
        PvStreamGEV *lStreamGEV = static_cast<PvStreamGEV *>( aStream );

        // Negotiate packet size
        lDeviceGEV->NegotiatePacketSize();

        // Configure device streaming destination
        lDeviceGEV->SetStreamDestination( lStreamGEV->GetLocalIPAddress(), lStreamGEV->GetLocalPort() );
    }
}

void CreateStreamBuffers( PvDevice *aDevice, PvStream *aStream, BufferList *aBufferList )
{
    // Reading payload size from device
    uint32_t lSize = aDevice->GetPayloadSize();

    // Use BUFFER_COUNT or the maximum number of buffers, whichever is smaller
    uint32_t lBufferCount = ( aStream->GetQueuedBufferMaximum() < BUFFER_COUNT ) ? 
        aStream->GetQueuedBufferMaximum() :
        BUFFER_COUNT;

    // Allocate buffers
    for ( uint32_t i = 0; i < lBufferCount; i++ )
    {
        // Create new buffer object
        PvBuffer *lBuffer = new PvBuffer;

        // Have the new buffer object allocate payload memory
        lBuffer->Alloc( static_cast<uint32_t>( lSize ) );
        
        // Add to external list - used to eventually release the buffers
        aBufferList->push_back( lBuffer );
    }
    
    // Queue all buffers in the stream
    BufferList::iterator lIt = aBufferList->begin();
    while ( lIt != aBufferList->end() )
    {
        aStream->QueueBuffer( *lIt );
        lIt++;
    }
}

void AcquireImages( PvDevice *aDevice, PvStream *aStream )
{
    // Get device parameters need to control streaming
    PvGenParameterArray *lDeviceParams = aDevice->GetParameters();

    // Map the GenICam AcquisitionStart and AcquisitionStop commands
    PvGenCommand *lStart = dynamic_cast<PvGenCommand *>( lDeviceParams->Get( "AcquisitionStart" ) );
    PvGenCommand *lStop = dynamic_cast<PvGenCommand *>( lDeviceParams->Get( "AcquisitionStop" ) );

    // Get stream parameters
    PvGenParameterArray *lStreamParams = aStream->GetParameters();

    // Map a few GenICam stream stats counters
    PvGenFloat *lFrameRate = dynamic_cast<PvGenFloat *>( lStreamParams->Get( "AcquisitionRate" ) );
    PvGenFloat *lBandwidth = dynamic_cast<PvGenFloat *>( lStreamParams->Get( "Bandwidth" ) );

    // Enable streaming and send the AcquisitionStart command
    cout << "Enabling streaming and sending AcquisitionStart command." << endl;
    aDevice->StreamEnable();
    lStart->Execute();

    char lDoodle[] = "|\\-|-/";
    int lDoodleIndex = 0;
    double lFrameRateVal = 0.0;
    double lBandwidthVal = 0.0;

    // Acquire images until the user instructs us to stop.
    cout << endl << "<press a key to stop streaming>" << endl;
    while ( !PvKbHit() )
    {
        PvBuffer *lBuffer = NULL;
        PvResult lOperationResult;

        // Retrieve next buffer
        PvResult lResult = aStream->RetrieveBuffer( &lBuffer, &lOperationResult, 1000 );
        if ( lResult.IsOK() )
        {
            if ( lOperationResult.IsOK() )
            {
                //
                // We now have a valid buffer. This is where you would typically process the buffer.
                // -----------------------------------------------------------------------------------------
                // ...

                lFrameRate->GetValue( lFrameRateVal );
                lBandwidth->GetValue( lBandwidthVal );

                cout << fixed << setprecision( 1 );
                cout << lDoodle[ lDoodleIndex ];
                cout << " BlockID: " << uppercase << hex << setfill( '0' ) << setw( 16 ) << lBuffer->GetBlockID();

                switch ( lBuffer->GetPayloadType() )
                {
                case PvPayloadTypeImage:
                    cout << "  W: " << dec << lBuffer->GetImage()->GetWidth() << " H: " << lBuffer->GetImage()->GetHeight();
                    break;

                case PvPayloadTypeChunkData:
                    cout << " Chunk Data payload type" << " with " << lBuffer->GetChunkCount() << " chunks";
                    break;

                case PvPayloadTypeRawData:
                    cout << " Raw Data with " << lBuffer->GetRawData()->GetPayloadLength() << " bytes";
                    break;

                case PvPayloadTypeMultiPart:
                    cout << " Multi Part with " << lBuffer->GetMultiPartContainer()->GetPartCount() << " parts";
                    break;

                default:
                    cout << " Payload type not supported by this sample";
                    break;
                }
                cout << "  " << lFrameRateVal << " FPS  " << ( lBandwidthVal / 1000000.0 ) << " Mb/s   \r";

                // Open the MP4 writer
                if( !mp4test.IsOpened() )
                {

                     if ( !mp4test.Open( "test.mp4", lBuffer->GetImage()) )
                      {
                           cout << "  open mp write is failed ";
                           break;
                      }
                }

                 if (!mp4test.WriteFrame( lBuffer->GetImage(), &lFileSizeDelta ))
                 {
                     cout << "  write  mp write is failed ";
                     break;
                 }
            }
            else
            {
                // Non OK operational result
                cout << lDoodle[ lDoodleIndex ] << " " << lOperationResult.GetCodeString().GetAscii() << "\r";
            }

            // Re-queue the buffer in the stream object
            aStream->QueueBuffer( lBuffer );
        }
        else
        {
            // Retrieve buffer failure
            cout << lDoodle[ lDoodleIndex ] << " " << lResult.GetCodeString().GetAscii() << "\r";
        }
     //   ImageSaving::SaveMp4( lBuffer );

        ++lDoodleIndex %= 6;
    }

    PvGetChar(); // Flush key buffer for next stop.
    cout << endl << endl;

    // Tell the device to stop sending images.
    cout << "Sending AcquisitionStop command to the device" << endl;
    lStop->Execute();

    // Disable streaming on the device
    cout << "Disable streaming on the controller." << endl;
    aDevice->StreamDisable();

    // Abort all buffers from the stream and dequeue
    cout << "Aborting buffers still in stream" << endl;
    aStream->AbortQueuedBuffers();
    while ( aStream->GetQueuedBufferCount() > 0 )
    {
        PvBuffer *lBuffer = NULL;
        PvResult lOperationResult;

        aStream->RetrieveBuffer( &lBuffer, &lOperationResult );
    }
}

void FreeStreamBuffers( BufferList *aBufferList )
{
    // Go through the buffer list
    BufferList::iterator lIt = aBufferList->begin();
    while ( lIt != aBufferList->end() )
    {
        delete *lIt;
        lIt++;
    }

    // Clear the buffer list 
    aBufferList->clear();
}


