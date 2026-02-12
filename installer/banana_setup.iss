[Setup]
AppName=Banana Programming Language
AppVersion=1.0.0
AppPublisher=Banana Language Team
AppPublisherURL=https://github.com/banana-language
AppSupportURL=https://github.com/banana-language/issues
AppUpdatesURL=https://github.com/banana-language/releases
DefaultDirName={pf}\Banana
DefaultGroupName=Banana Language
AllowNoIcons=yes
OutputBaseFilename=Banana-Setup-1.0.0
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ChangesEnvironment=yes

[Files]
Source: "bin\banana.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "src\*.py"; DestDir: "{app}\src"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "mode\*.BMDe"; DestDir: "{app}\mode"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "tests\*.baNa"; DestDir: "{app}\tests"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "examples\*.baNa"; DestDir: "{app}\examples"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "docs\*"; DestDir: "{app}\docs"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "resources\*"; DestDir: "{app}\resources"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Banana Language"; Filename: "{app}\banana.exe"
Name: "{group}\Banana Documentation"; Filename: "{app}\docs\README.md"
Name: "{group}\Uninstall Banana Language"; Filename: "{uninstallexe}"

[Registry]
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: NeedsAddPath('{app}')

[Run]
Filename: "{app}\banana.exe"; Description: "Launch Banana Language"; Flags: nowait postinstall skipifsilent

[Code]
function NeedsAddPath(Param: string): boolean;
var
  OrigPath: string;
begin
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path', OrigPath) then
  begin
    Result := True;
    exit;
  end;
  Result := Pos(';' + Param + ';', ';' + OrigPath + ';') = 0;
  if Result = True then
    Result := Pos(';' + Param + '\;', ';' + OrigPath + ';') = 0;
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  ResultCode: Integer;
begin
  if CurStep = ssPostInstall then
  begin
    if NeedsAddPath(ExpandConstant('{app}')) then
    begin
      RegWriteExpandStringValue(HKEY_LOCAL_MACHINE,
        'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
        'Path',
        ExpandConstant('{app};') + 
        RegQueryStringValue(HKEY_LOCAL_MACHINE,
          'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
          'Path'));
      
      MsgBox('Banana Language has been added to system PATH. Please restart your computer or log off and log on again for changes to take effect.', mbInformation, MB_OK);
    end;
  end;
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
var
  Path: string;
begin
  if CurUninstallStep = usUninstall then
  begin
    if RegQueryStringValue(HKEY_LOCAL_MACHINE,
      'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
      'Path', Path) then
    begin
      Path := StringReplace(Path, ExpandConstant('{app};'), '', [rfReplaceAll, rfIgnoreCase]);
      Path := StringReplace(Path, ExpandConstant('{app}'), '', [rfReplaceAll, rfIgnoreCase]);
      RegWriteExpandStringValue(HKEY_LOCAL_MACHINE,
        'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
        'Path', Path);
    end;
  end;
end;
