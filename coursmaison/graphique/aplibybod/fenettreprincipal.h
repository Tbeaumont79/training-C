#ifndef FENETTREPRINCIPAL_H
#define FENETTREPRINCIPAL_H

#include <QMainWindow>

namespace Ui {
class Fenettreprincipal;
}

class Fenettreprincipal : public QMainWindow
{
    Q_OBJECT

public:
    explicit Fenettreprincipal(QWidget *parent = 0);
    ~Fenettreprincipal();

private:
    Ui::Fenettreprincipal *ui;
};

#endif // FENETTREPRINCIPAL_H
void CustomWidget::paintEvent(QPaintEvent *)
{
    QStyleOption opt;
    opt.init(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget, &opt, &p, this);
}
