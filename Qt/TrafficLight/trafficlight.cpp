#include "trafficlight.h"
#include "ui_trafficlight.h"

TrafficLight::TrafficLight(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::TrafficLight)
{
    ui->setupUi(this);
}

TrafficLight::~TrafficLight()
{
    delete ui;
}

