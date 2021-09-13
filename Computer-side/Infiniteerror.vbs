
Function infiniteerrors()
' Toggles another vbs file infinitely and shows infinite errors 
    Dim x, Wshell
    x = 1
    Set Wshell = WScript.CreateObject("Wscript.Shell")
    Do Until x > 5    
        For i = 1 To 5
        call Wshell.Run("Window.vbs")
        Next
    Loop
    Set Wshell = Nothing
End Function

Function main()
'  Main Function all code runs here
    dim mensaje
    mensaje = MsgBox("You're about to get infinite errors", 64, "Error")
    If mensaje = 1 Then
        Call infiniteerrors
        End If
End Function

Call main