#include <bits/stdc++.h>

int main(void)

{
  long lVar1;
  FILE *fileCheck;
  FILE *picCheck;
  size_t sVar2;
  long in_FS_OFFSET;
  int j;
  int i;
  char data[26];

  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  fileCheck = fopen("flag.txt", "r");
  picCheck = fopen("mystery.png", "a");
  if (fileCheck == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (picCheck == (FILE *)0x0) {
    puts("mystery.png is missing, please run this on the server");
  }
  sVar2 = fread(data, 0x1a, 1, fileCheck);
  if ((int)sVar2 < 1) {
    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("at insert");
  fputc((int)data[0], picCheck);
  fputc((int)data[1], picCheck);
  fputc((int)data[2], picCheck);
  fputc((int)data[3], picCheck);
  fputc((int)data[4], picCheck);
  fputc((int)data[5], picCheck);
  for (j = 6; j < 15; j = j + 1) {
    fputc((int)(char)(data[j] + 5), picCheck);
  }
  fputc((int)(char)(data[0xf] + -3), picCheck);
  for (i = 16; i < 26; i = i + 1) {
    fputc((int)data[i], picCheck);
  }
  fclose(picCheck);
  fclose(fileCheck);
  if (lVar1 != *(long *)(in_FS_OFFSET + 40)) {
    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
