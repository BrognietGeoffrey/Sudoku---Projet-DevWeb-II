<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>130</y>
      <width>701</width>
      <height>261</height>
     </rect>
    </property>
    <column>
     <property name="text">
      <string>Date de jeu</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Commentaire</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Score</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Image</string>
     </property>
    </column>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>30</y>
      <width>629</width>
      <height>87</height>
     </rect>
    </property>
    <property name="html">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:18pt; font-weight:600; text-decoration: underline;&quot;&gt;PLAYER WINDOW&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>420</y>
      <width>161</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>See New Games</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>480</x>
      <y>420</y>
      <width>201</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Start New Game</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menuplayer_window">
    <property name="title">
     <string>player_window</string>
    </property>
   </widget>
   <addaction name="menuplayer_window"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
