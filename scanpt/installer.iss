[Setup]
AppName=scanpt
AppVersion=1.0
DefaultDirName={pf}\scanpt
DefaultGroupName=scanpt
OutputDir=dist
OutputBaseFilename=scanpt-setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\scanpt.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\scanpt"; Filename: "{app}\scanpt.exe"

[Run]
Filename: "{app}\scanpt.exe"; Description: "Ejecutar scanpt"; Flags: nowait postinstall skipifsilent
