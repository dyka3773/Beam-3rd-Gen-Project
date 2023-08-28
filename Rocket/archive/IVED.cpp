#include <iostream>
#include <labjackusb.h>

int main() {
    LJ_HANDLE ljHandle;
    long error;
    long valueAIN0, valueAIN1, valueGND, valueSGND, valueVS;

    // Open the LabJack U3
    error = OpenLabJack(LJ_dtU3, LJ_ctUSB, "1", 1, &ljHandle);
    if (error != 0) {
        std::cout << "Failed to open LabJack. Error code: " << error << std::endl;
        return 1;
    }

    // Configure AIN0, AIN1, GND, SGND, and VS as analog inputs
    error = ePut(ljHandle, LJ_ioPUT_ANALOG_ENABLE_BIT, 0, 31, 5);
    if (error != 0) {
        std::cout << "Failed to configure analog inputs." << error << std::endl;
        CloseLabJack(ljHandle);
        return 1;
    }

    // Read analog inputs
    error = eAIN(ljHandle, 0, 31, &valueAIN0, 0, 0, 0, 0);
    error |= eAIN(ljHandle, 1, 31, &valueAIN1, 0, 0, 0, 0);
    error |= eAIN(ljHandle, 2, 31, &valueGND, 0, 0, 0, 0);
    error |= eAIN(ljHandle, 3, 31, &valueSGND, 0, 0, 0, 0);
    error |= eAIN(ljHandle, 32, 31, &valueVS, 0, 0, 0, 0);

    if (error != 0) {
        std::cout << "Failed to read analog inputs." << error << std::endl;
        CloseLabJack(ljHandle);
        return 1;
    }

    // Print the measured values
    std::cout << "AIN0: " << valueAIN0 << std::endl;
    std::cout << "AIN1: " << valueAIN1 << std::endl;
    std::cout << "GND: " << valueGND << std::endl;
    std::cout << "SGND: " << valueSGND << std::endl;
    std::cout << "VS (Voltage Sum): " << valueVS << std::endl;

    // Close the LabJack U3
    CloseLabJack(ljHandle);

    return 0;
}