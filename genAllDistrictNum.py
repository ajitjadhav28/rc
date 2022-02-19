from itertools import combinations_with_replacement

clear_input = "adb shell input keyevent 67\n" * 10
search_bar = "adb shell input touchscreen tap 750 410\n"
search_input = 'adb shell input text "MH14{rc_num}7941"\n'
search_button = "adb shell input touchscreen tap 910 410\n"
sleep_sec = "sleep {sec}\n"
warn_ok = "adb shell input touchscreen tap 500 1400\n"
take_sc = "adb exec-out screencap -p > MH14{rc_num}7941.png\n"

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

shell_cmd = open('shell_run.sh', 'w+')

for vec in combinations_with_replacement(alphabets, 2):
    shell_cmd.write(search_bar
        + clear_input 
        + search_input.format(rc_num=''.join(vec))
        + search_button
        + sleep_sec.format(sec = 2)
        + warn_ok
        + sleep_sec.format(sec = 3)
        + take_sc.format(rc_num = ''.join(vec))
        + sleep_sec.format(sec = 2)
        + 'echo "Done for MH14{}7941 RC"\n'.format(''.join(vec))
        )

shell_cmd.close()