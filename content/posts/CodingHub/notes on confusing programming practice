Title: Notes on Confusing Programming Practice
Tags: linux; python

## grep -E '\.lbl$' input.txt > output.txt
Though there were many lines like "xxx.lbl" in input.txt, but I got an empty file of output.txt. This was because that the input.txt was uploaded from windows. So, the line break in input.txt is 'windows' style (i.e., Carriage Return + Line Feed, or \r\n). I ran `cat -A input.xt`, and I found that it printed like "xxx.lbl^M$". This is the reason that '$' cannot match with '^M'.

**Solve**: Use `dos2unix input.txt ` to translate the windows-style line-bread into unix-style ones. Then, run the grep command to continue.