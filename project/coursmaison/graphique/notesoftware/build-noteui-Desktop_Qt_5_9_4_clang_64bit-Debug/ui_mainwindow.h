/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.9.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *fenetrePrincipale;
    QGridLayout *gridLayout;
    QPushButton *btn_addnote;
    QPushButton *btn_removenote;
    QListWidget *lw_listeDeNotes;
    QTextEdit *te_contenuDeLaNote;
    QPushButton *btn_updatenote;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(609, 516);
        fenetrePrincipale = new QWidget(MainWindow);
        fenetrePrincipale->setObjectName(QStringLiteral("fenetrePrincipale"));
        gridLayout = new QGridLayout(fenetrePrincipale);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        btn_addnote = new QPushButton(fenetrePrincipale);
        btn_addnote->setObjectName(QStringLiteral("btn_addnote"));

        gridLayout->addWidget(btn_addnote, 0, 0, 1, 1);

        btn_removenote = new QPushButton(fenetrePrincipale);
        btn_removenote->setObjectName(QStringLiteral("btn_removenote"));

        gridLayout->addWidget(btn_removenote, 0, 1, 1, 1);

        lw_listeDeNotes = new QListWidget(fenetrePrincipale);
        lw_listeDeNotes->setObjectName(QStringLiteral("lw_listeDeNotes"));

        gridLayout->addWidget(lw_listeDeNotes, 1, 0, 2, 2);

        te_contenuDeLaNote = new QTextEdit(fenetrePrincipale);
        te_contenuDeLaNote->setObjectName(QStringLiteral("te_contenuDeLaNote"));

        gridLayout->addWidget(te_contenuDeLaNote, 1, 2, 1, 1);

        btn_updatenote = new QPushButton(fenetrePrincipale);
        btn_updatenote->setObjectName(QStringLiteral("btn_updatenote"));

        gridLayout->addWidget(btn_updatenote, 2, 2, 1, 1);

        MainWindow->setCentralWidget(fenetrePrincipale);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 609, 22));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        mainToolBar->setEnabled(false);
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        statusBar->setEnabled(false);
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Note creator", Q_NULLPTR));
        btn_addnote->setText(QApplication::translate("MainWindow", "add note", Q_NULLPTR));
        btn_removenote->setText(QApplication::translate("MainWindow", "remove note", Q_NULLPTR));
        btn_updatenote->setText(QApplication::translate("MainWindow", "update note", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
