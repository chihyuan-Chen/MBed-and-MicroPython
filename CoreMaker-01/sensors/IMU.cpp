/* 
 * MIT License
 *
 * Copyright (c) 2022 CoretronicMEMS
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
*/
#include "global.h"
#include "IMU.h"
#include "mbed.h"
#include "drivers/BufferedSerial.h"
BufferedSerial device(MIKOR_TX, MIKOR_RX, 9600);
BufferedSerial device_1(CONSOLE_TX, CONSOLE_RX, 115200);

namespace CMC
{
    IMU::IMU(PinName RX, PinName TX, int odr):
        m_ODR(odr)
    {
    }

    IMU::~IMU()
    {

    }

    int32_t IMU::Initialize()
    {
        SetODR(m_ODR);
        DBG_MSG("%s initialized\n", Name());
        return 0;
    }

    int32_t IMU::Uninitialize()
    {  
        return 0;
    }

    int32_t IMU::Write(const void *data, size_t num)
    {
        return 0;
    }

    int32_t IMU::Read(void *data, size_t num)
    {
        return ReadData((float *)data, num);
    }

    int32_t IMU::Control(uint32_t control, uint32_t arg)
    {
        if (control == SENSOR_CTRL_START)
        {
            m_timer.attach(callback(this, &IMU::TimerCallback), std::chrono::microseconds((int)(1000000/m_ODR)));
            m_isOn = true;
        }
        else if (control == SENSOR_CTRL_STOP)
        {
            m_timer.detach();
            m_isOn = false;
        }
        else if (control == SENSOR_CTRL_SET_ODR)
        {
            if(m_isOn)
                m_timer.detach();
            int32_t odr = SetODR(arg);
            if(m_isOn)
                m_timer.attach(callback(this, &IMU::TimerCallback), std::chrono::microseconds((int)(1000000/m_ODR)));
            return odr;
        }
        else if (control == SENSOR_CTRL_SELFTEST)
        {
            return SelftTest();
        }
        else if (control == SENSOR_CTRL_GET_ODR)
        {
            *((uint32_t*)arg) = m_ODR;
        }
        else if (control == SENSOR_CTRL_SET_GAIN)
        {
        }
        return 0;
    }

    int32_t IMU::ReadData(float *data, uint32_t num)
    {
        char str[6];
        char buffer[6];
        if(device.readable())
        {
            device.read(&buffer, sizeof(buffer));
            if(buffer[sizeof(buffer)-1] == '\n')
            {
                buffer[sizeof(buffer)-1] = '0';
                strcpy(str, buffer);
                data[0] = atof(str);
                device_1.write(str, sizeof(str));
            }
            return 1;
        }
        return -1;
    }

    int32_t IMU::SetODR(uint32_t arg)
    {
        m_ODR = arg;
        return m_ODR;
    }

    int32_t IMU::SelftTest()
    {
        float *data;
        ReadData(data, 1);
        printf("%.2f\n", *data);

        return 1;
    }

    void IMU::TimerCallback()
    {
        SetDataReady();
    }

}; //namespace CMC
