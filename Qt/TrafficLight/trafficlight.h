#ifndef TRAFFICLIGHT_H
#define TRAFFICLIGHT_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class TrafficLight; }
QT_END_NAMESPACE

class TrafficLight : public QMainWindow
{
    Q_OBJECT

public:
    TrafficLight(QWidget *parent = nullptr);
    ~TrafficLight();

private:
    Ui::TrafficLight *ui;
};
#endif // TRAFFICLIGHT_H
