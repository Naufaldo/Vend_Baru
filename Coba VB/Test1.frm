VERSION 5.00
Object = "{648A5603-2C6E-101B-82B6-000000000014}#1.1#0"; "MSCOMM32.OCX"
Begin VB.Form Form1 
   BackColor       =   &H0000FF00&
   Caption         =   "Form1"
   ClientHeight    =   10785
   ClientLeft      =   -4590
   ClientTop       =   -2250
   ClientWidth     =   19200
   LinkTopic       =   "Form1"
   Picture         =   "Test1.frx":0000
   ScaleHeight     =   720
   ScaleMode       =   0  'User
   ScaleWidth      =   1280
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command2 
      BackColor       =   &H80000001&
      DisabledPicture =   "Test1.frx":18841
      DownPicture     =   "Test1.frx":1A9CA
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1335
      Left            =   6360
      MaskColor       =   &H00FF8080&
      Picture         =   "Test1.frx":1CB53
      Style           =   1  'Graphical
      TabIndex        =   1
      Top             =   8640
      UseMaskColor    =   -1  'True
      Width           =   4575
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H8000000E&
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   17760
      Picture         =   "Test1.frx":1ECDC
      Style           =   1  'Graphical
      TabIndex        =   0
      Top             =   9000
      Width           =   1095
   End
   Begin MSCommLib.MSComm MSComm1 
      Left            =   240
      Top             =   1320
      _ExtentX        =   1005
      _ExtentY        =   1005
      _Version        =   393216
      DTREnable       =   -1  'True
      BaudRate        =   115200
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
MSComm1.Output = "9"
End Sub
Private Sub Command2_Click()
MSComm1.Output = "1"
End Sub

Private Sub Form_Load()
    If MSComm1.PortOpen = False Then
       MSComm1.PortOpen = True
       MSComm1.Output = "0"
    End If

End Sub

Private Sub Form_Unload(Cancel As Integer)
     If MSComm1.PortOpen = True Then
       MSComm1.PortOpen = False
     End If
End Sub

