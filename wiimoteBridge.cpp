/* Copyright 2025 by Charles Descamps */
#include <cwiid.h>
#include <iostream>
#include <unistd.h>

#define BUTTON_DELAY 200000 // 0.2 seconds in microseconds

void connect_wiimote(cwiid_wiimote_t** wiimote, int& attempts, const char* wiimote_name) 
{
    while (!*wiimote) 
    {
        bdaddr_t bdaddr = *BDADDR_ANY;
        *wiimote = cwiid_open(&bdaddr, CWIID_FLAG_MESG_IFC);
        if (!*wiimote) 
        {
            if (attempts > 10) 
            {
                std::cout << wiimote_name << " is not connected, moving on." << std::endl;
                break;
            }
            std::cout << "Error connecting " << wiimote_name << std::endl;
            std::cout << "On attempt " << attempts << std::endl;
            attempts++;
        }
    }
}

void set_rumble(cwiid_wiimote_t* wiimote, bool rumble_on) 
{
    if (wiimote) 
    {
        cwiid_command(wiimote, CWIID_CMD_RUMBLE, rumble_on ? 1 : 0);
    }
}

int main() 
{
    cwiid_wiimote_t* wiimoteOne = nullptr;
    cwiid_wiimote_t* wiimoteTwo = nullptr;
    cwiid_wiimote_t* wiimoteThree = nullptr;
    cwiid_wiimote_t* wiimoteFour = nullptr;

    int wiimoteOneAttempts = 2;
    int wiimoteTwoAttempts = 2;
    int wiimoteThreeAttempts = 2;
    int wiimoteFourAttempts = 2;

    std::cout << "Press 1+2 on Wiimotes to connect." << std::endl;

    connect_wiimote(&wiimoteOne, wiimoteOneAttempts, "Wiimote One");
    connect_wiimote(&wiimoteTwo, wiimoteTwoAttempts, "Wiimote Two");
    connect_wiimote(&wiimoteThree, wiimoteThreeAttempts, "Wiimote Three");
    connect_wiimote(&wiimoteFour, wiimoteFourAttempts, "Wiimote Four");

    if (wiimoteOne) cwiid_set_rpt_mode(wiimoteOne, CWIID_RPT_BTN);
    if (wiimoteTwo) cwiid_set_rpt_mode(wiimoteTwo, CWIID_RPT_BTN);
    if (wiimoteThree) cwiid_set_rpt_mode(wiimoteThree, CWIID_RPT_BTN);
    if (wiimoteFour) cwiid_set_rpt_mode(wiimoteFour, CWIID_RPT_BTN);

    if (wiimoteOne) cwiid_set_led(wiimoteOne, CWIID_LED1_ON);
    if (wiimoteTwo) cwiid_set_led(wiimoteTwo, CWIID_LED2_ON);
    if (wiimoteThree) cwiid_set_led(wiimoteThree, CWIID_LED3_ON);
    if (wiimoteFour) cwiid_set_led(wiimoteFour, CWIID_LED4_ON);

    while (true) 
    {
        cwiid_state stateOne, stateTwo, stateThree, stateFour;

        if (wiimoteOne) cwiid_get_state(wiimoteOne, &stateOne);
        if (wiimoteTwo) cwiid_get_state(wiimoteTwo, &stateTwo);
        if (wiimoteThree) cwiid_get_state(wiimoteThree, &stateThree);
        if (wiimoteFour) cwiid_get_state(wiimoteFour, &stateFour);

        unsigned int wiimoteOneButtons = wiimoteOne ? stateOne.buttons : 0;
        unsigned int wiimoteTwoButtons = wiimoteTwo ? stateTwo.buttons : 0;
        unsigned int wiimoteThreeButtons = wiimoteThree ? stateThree.buttons : 0;
        unsigned int wiimoteFourButtons = wiimoteFour ? stateFour.buttons : 0;

        unsigned int wiimoteOneExitState = wiimoteOneButtons & (CWIID_BTN_PLUS | CWIID_BTN_MINUS);
        unsigned int wiimoteTwoExitState = wiimoteTwoButtons & (CWIID_BTN_PLUS | CWIID_BTN_MINUS);
        unsigned int wiimoteThreeExitState = wiimoteThreeButtons & (CWIID_BTN_PLUS | CWIID_BTN_MINUS);
        unsigned int wiimoteFourExitState = wiimoteFourButtons & (CWIID_BTN_PLUS | CWIID_BTN_MINUS);

        if (wiimoteOneExitState == (CWIID_BTN_PLUS | CWIID_BTN_MINUS) ||
            wiimoteTwoExitState == (CWIID_BTN_PLUS | CWIID_BTN_MINUS) ||
            wiimoteThreeExitState == (CWIID_BTN_PLUS | CWIID_BTN_MINUS) ||
            wiimoteFourExitState == (CWIID_BTN_PLUS | CWIID_BTN_MINUS)) 
        {
            if (wiimoteOneExitState == (CWIID_BTN_PLUS | CWIID_BTN_MINUS)) 
            {
                std::cout << "Wiimote One Connection Closing" << std::endl;
                set_rumble(wiimoteOne, true);
                usleep(500000);
                set_rumble(wiimoteOne, false);
                cwiid_close(wiimoteOne);
            } 
            else if (wiimoteTwoExitState == (CWIID_BTN_PLUS | CWIID_BTN_MINUS)) 
            {
                std::cout << "Wiimote Two Connection Closing" << std::endl;
                set_rumble(wiimoteTwo, true);
                usleep(500000);
                set_rumble(wiimoteTwo, false);
                cwiid_close(wiimoteTwo);
            } 
            else if (wiimoteThreeExitState == (CWIID_BTN_PLUS | CWIID_BTN_MINUS)) 
            {
                std::cout << "Wiimote Three Connection Closing" << std::endl;
                set_rumble(wiimoteThree, true);
                usleep(500000);
                set_rumble(wiimoteThree, false);
                cwiid_close(wiimoteThree);
            } 
            else 
            {
                std::cout << "Wiimote Four Connection Closing" << std::endl;
                set_rumble(wiimoteFour, true);
                usleep(500000);
                set_rumble(wiimoteFour, false);
                cwiid_close(wiimoteFour);
            }
            break;
        }

        // Check button states (Button A pressed or Button B pressed)
        bool wiimoteOnePressA = wiimoteOneButtons & CWIID_BTN_A;
        bool wiimoteOnePressB = wiimoteOneButtons & CWIID_BTN_B;
        bool wiimoteTwoPressA = wiimoteTwoButtons & CWIID_BTN_A;
        bool wiimoteTwoPressB = wiimoteTwoButtons & CWIID_BTN_B;
        bool wiimoteThreePressA = wiimoteThreeButtons & CWIID_BTN_A;
        bool wiimoteThreePressB = wiimoteThreeButtons & CWIID_BTN_B;
        bool wiimoteFourPressA = wiimoteFourButtons & CWIID_BTN_A;
        bool wiimoteFourPressB = wiimoteFourButtons & CWIID_BTN_B;

        if (wiimoteOnePressA || wiimoteOnePressB) 
        {
            // DO SOMETHING
            std::cout << "Wiimote One Pressed A or B!" << std::endl;
        } 
        if (wiimoteTwoPressA || wiimoteTwoPressB) 
        {
            // DO SOMETHING
            std::cout << "Wiimote Two Pressed A or B!" << std::endl;
        } 
        if (wiimoteThreePressA || wiimoteThreePressB) 
        {
            // DO SOMETHING
            std::cout << "Wiimote Three Pressed A or B!" << std::endl;
        } 
        if (wiimoteFourPressA || wiimoteFourPressB) 
        {
            // DO SOMETHING
            std::cout << "Wiimote Four Pressed A or B!" << std::endl;
        }

        usleep(BUTTON_DELAY);
    }

    return 0;
}