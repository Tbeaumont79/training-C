#include "fenettreprincipal.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Fenettreprincipal w;
    w.show();

    return a.exec();
}
