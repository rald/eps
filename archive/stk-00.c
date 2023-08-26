#include <stdio.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <ctype.h>

#define MX 160

uint8_t m[MX]={0};

typedef struct stk_t stk_t;

struct stk_t {
  uint16_t s;
  uint16_t b;
  uint16_t e;
  uint16_t t;
};

stk_t *stk=NULL;

stk_t *stkn(uint16_t b,uint16_t s) {
  stk_t *stk=malloc(sizeof(*stk));
  if(stk) {
    stk->s=s>MX?MX:s;
    stk->b=b%MX;
    stk->e=(b+s)%MX;
    stk->t=stk->e;
  }
  return stk;
}

void stkf(stk_t **s) {
  free(*s);
  *s=NULL;
}

int pub(stk_t *s,uint8_t v) {
  if(s->t==s->b) {
    printf("stack overflow\n");
    return -1;
  }
  s->t=(s->t-1)%MX;
  m[s->t]=v;
  printf("pub %02x\n",v);
  return 0;
}

int ppb(stk_t *s,uint8_t *v) {
  if (s->t==stk->e) {
    printf("stack underflow\n");
    return -1;
  }
  *v=m[s->t];
  s->t=((uint16_t)s->t+1)%MX;
  printf("ppb %02x\n",*v);
  return 0;
}



void dump() {
  uint16_t i=0;
  int j=0;
  char s[17];
  char c='\0';
  s[0]='\0';

  printf("\x1b[37;40m");
  while(i<MX) {

    if(i!=0 && i%16==0) printf("\n");
    if(i%16==0) printf("\x1b[1;37;40m%04x  ",i);
    if(i>=stk->b)
      printf("\x1b[33;44m");
    else if(i<=stk->b+stk->s-1)
      printf("\x1b[37;40m");
    
   if(i==stk->t)
      printf(">%02x",m[i]);
    else
      printf(" %02x",m[i]);
 
    c=m[i];
    if(!isalnum(c) && !ispunct(c)) c='.';
    
    s[j++]=c;
    s[j]='\0';

    if(j==16) {
      printf("\x1b[37;40m  '%s'",s);
      s[0]='\0';
      j=0;
    }
    i++;
  }
  if(j) printf("\x1b[37;40m  '%s'",s);
  printf("\n");
  printf("\x1b[0m");

}


int main() {

  stk=stkn(MX-16,16);

  pub(stk,0x31);

//  dump();

  stkf(&stk);

  return 0;
}
