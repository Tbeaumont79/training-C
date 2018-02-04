/********************************************************************************
** Form generated from reading UI file 'fenettreprincipal.ui'
**
** Created by: Qt User Interface Compiler version 5.9.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FENETTREPRINCIPAL_H
#define UI_FENETTREPRINCIPAL_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Fenettreprincipal
{
public:
    QWidget *centralWidget;
    QListWidget *playList;
    QProgressBar *time_music;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QTextBrowser *textBrowser;

    void setupUi(QMainWindow *Fenettreprincipal)
    {
        if (Fenettreprincipal->objectName().isEmpty())
            Fenettreprincipal->setObjectName(QStringLiteral("Fenettreprincipal"));
        Fenettreprincipal->resize(618, 522);
        Fenettreprincipal->setStyleSheet(QStringLiteral(""));
        centralWidget = new QWidget(Fenettreprincipal);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        playList = new QListWidget(centralWidget);
        playList->setObjectName(QStringLiteral("playList"));
        playList->setGeometry(QRect(40, 80, 531, 251));
        playList->setAutoFillBackground(false);
        time_music = new QProgressBar(centralWidget);
        time_music->setObjectName(QStringLiteral("time_music"));
        time_music->setGeometry(QRect(50, 410, 521, 23));
        time_music->setValue(24);
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(160, 360, 80, 24));
        pushButton_2 = new QPushButton(centralWidget);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(360, 360, 80, 24));
        pushButton_3 = new QPushButton(centralWidget);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setGeometry(QRect(260, 360, 80, 24));
        textBrowser = new QTextBrowser(centralWidget);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));
        textBrowser->setGeometry(QRect(220, 10, 171, 31));
        Fenettreprincipal->setCentralWidget(centralWidget);

        retranslateUi(Fenettreprincipal);

        QMetaObject::connectSlotsByName(Fenettreprincipal);
    } // setupUi

    void retranslateUi(QMainWindow *Fenettreprincipal)
    {
        Fenettreprincipal->setWindowTitle(QApplication::translate("Fenettreprincipal", "application 1", Q_NULLPTR));
        pushButton->setText(QApplication::translate("Fenettreprincipal", "play", Q_NULLPTR));
        pushButton_2->setText(QApplication::translate("Fenettreprincipal", "repeat", Q_NULLPTR));
        pushButton_3->setText(QApplication::translate("Fenettreprincipal", "stop", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class Fenettreprincipal: public Ui_Fenettreprincipal {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FENETTREPRINCIPAL_H
