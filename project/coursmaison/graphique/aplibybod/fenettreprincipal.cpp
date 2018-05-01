#include "fenettreprincipal.h"
#include "ui_fenettreprincipal.h"

Fenettreprincipal::Fenettreprincipal(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Fenettreprincipal)
{
    ui->setupUi(this);
}

Fenettreprincipal::~Fenettreprincipal()
{
    delete ui;
}
