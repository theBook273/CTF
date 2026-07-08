#include <bits/stdc++.h>

signed main(void)

{
  size_t sVar1;
  long in_FS_OFFSET;
  char local_7e;
  char local_7d;
  int local_7c;
  int loop1;
  int i;
  int j;
  signed local_6c;
  int lim;
  int local_64;
  FILE *flag;
  FILE *original;
  FILE *encoded;
  char array[56];
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 40);
  local_6c = 0;
  flag = fopen("flag.txt", "r");
  original = fopen("original.bmp", "r");
  encoded = fopen("encoded.bmp", "a");
  if (flag == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (original == (FILE *)0x0) {
    puts("original.bmp is missing, please run this on the server");
  }
  sVar1 = fread(&local_7e, 1, 1, original);
  local_7c = (int)sVar1;
  lim = 2000;
  for (loop1 = 0; loop1 < lim; loop1 = loop1 + 1) {
    fputc((int)local_7e, encoded);
    sVar1 = fread(&local_7e, 1, 1, original);
    local_7c = (int)sVar1;
  }
  sVar1 = fread(array, 50, 1, flag);
  local_64 = (int)sVar1;
  if (local_64 < 1) {
    puts("flag is not 50 chars");
    exit(0);
  }
  for (i = 0; i < 50; i = i + 1) {
    for (j = 0; j < 8; j = j + 1) {
      local_7d = codedChar(j, (int)(char)(array[i] + -5), (int)local_7e);
      fputc((int)local_7d, encoded);
      fread(&local_7e, 1, 1, original);
    }
  }
  while (local_7c == 1) {
    fputc((int)local_7e, encoded);
    sVar1 = fread(&local_7e, 1, 1, original);
    local_7c = (int)sVar1;
  }
  fclose(encoded);
  fclose(original);
  fclose(flag);
  if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
    return 0;
  }
  /* WARNING: Subroutine does not return */
  // __stack_chk_fail();
}
