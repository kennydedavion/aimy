#include <ros.h>
#include <std_msgs/String.h>
#include <Wire.h>
const int MPU_addr=0x68 ;  
int16_t ACX,ACY,ACZ,Tmp,GyX,GyY,GyZ;
//Set up the ros node and publisher
std_msgs::String imu_msg;
ros::Publisher imu("imu", &imu_msg);
ros::NodeHandle nh;
                           
void setup()
{
  nh.initNode();
  nh.advertise(imu);
  
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Serial.begin(9600);
}
long publisher_timer;
void loop()
{
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers  String AX = String(mpu6050.getAccX());
  
  ACX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
  ACY=Wire.read()<<8|Wire.read();
  ACZ=Wire.read()<<8|Wire.read();
  Tmp=Wire.read()<<8|Wire.read();
  GyX=Wire.read()<<8|Wire.read();
  GyY=Wire.read()<<8|Wire.read();
  GyZ=Wire.read()<<8|Wire.read();
  String AX = String(ACX);
  String AY = String(ACY);
  String AZ = String(ACZ);
  String GX = String(GyX);
  String GY = String(GyY);
  String GZ = String(GyZ);
  String tmp = String(Tmp);
  String data = "A" + AX + "B"+ AY + "C" + AZ + "D" + GX + "E" + GY + "F" + GZ + 
  Serial.println(data
  int length = data.indexOf("G");
  char data_final[data.toCharArray(data_final, length+1);
  
  if (millis() > publisher_timer) {
    // step 1: request reading from sensor
    imu_msg.
    imu.publish(&imu_msg
    publisher_timer = millis() + 100;
    nh.spinOnce()
  }
  
}
