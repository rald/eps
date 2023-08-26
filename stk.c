#include <stdio.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

uint16_t mx=160;

uint8_t *m;

typedef struct stk_t stk_t;

struct stk_t {
  uint16_t s;
  uint16_t b;
  uint16_t e;
  uint16_t t;
};

stk_t *stk=NULL;

stk_t *stkn(uint16_t b,uint16_t e) {
  stk_t *stk=malloc(sizeof(*stk));
  if(stk) {
    stk->b=b%mx;
    stk->e=e%mx;
    stk->t=stk->e;
    stk->s=(stk->e>=stk->b?stk->e-stk->b:stk->b-stk->e)+1;
  }
  return stk;
}

void stkf(stk_t **s) {
  free(*s);
  *s=NULL;
}

int pub(stk_t *s,uint8_t v) {
  printf("pub %02X\n",v);
  if(s->t==s->b) {
    printf("stack overflow\n");
    return 1;
  }
  if(s->t==0) s->t=mx-1; else s->t--;
  m[s->t]=v;
  return 0;
}

int ppb(stk_t *s,uint8_t *v) {
  if (s->t==stk->e) {
    printf("stack underflow\n");
    return 1;
  }
  *v=m[s->t];
  printf("ppb %02X\n",*v);
  if(s->t==mx-1) s->t=0; else s->t++;
  return 0;
}

void dump() {
  uint16_t i=0;
  int j=0;
  char s[18];
  char c='\0';
  s[0]='\0';

  printf("\n");
  printf("\x1b[37;40m");
  while(i<mx) {
    if(i!=0 && i%16==0) printf("\n");
    if(i%16==0) printf("\x1b[1;37;40m%04X ",i);
    if(i%8==0) printf("  ");

    if(i==stk->t)
      printf("\x1b[31;47m%02X",m[i]);
    else if(stk->b>stk->e && i<=stk->e)
      printf("\x1b[37;45m%02X",m[i]);
    else if(stk->b>stk->e && i>=stk->b)
      printf("\x1b[37;45m%02X",m[i]);
    else if(i>=stk->b && i<=stk->e)
      printf("\x1b[37;45m%02X",m[i]);
    else
      printf("\x1b[37;40m%02X",m[i]);

    printf(" ");
 
    c=m[i];
    if(!isalnum(c) && !ispunct(c)) c='.';
    
    s[j++]=c;
    if(j==8) s[j++]=' ';
    s[j]='\0';

    if(j==17) {
      printf("\x1b[37;40m  %s",s);
      s[0]='\0';
      j=0;
    }
    i++;
  }
  for(int k=0;k<17-j;k++) {
    if(k==8)
      printf("  ");
    else
      printf("   ");
  }

  if(j) printf("\x1b[37;40m  %s",s);
  printf("\n");
  printf("\x1b[0m");
  printf("\n");
}

void do_pushb() {
  unsigned int b;
  do {
    printf("Enter hex byte (00-FF): ");
  } while(scanf("%02x",&b)!=1);
  pub(stk,b%256);
}

void do_popb() {
  uint8_t v;
  ppb(stk,&v);
}

void do_realloc() {
  unsigned int w;
  do {
    printf("Enter hex byte (0000-FFFF): ");
  } while(scanf("%04x",&w)!=1);
  mx=w%65536;
  m=realloc(m,sizeof(*m)*mx);
}

void do_new_stack() {
  unsigned int b;
  unsigned int e;
  do {
    printf("Enter hex byte (0000-FFFF): ");
  } while(scanf("%04x",&b)!=1);
  do {
    printf("Enter hex byte (0000-FFFF): ");
  } while(scanf("%04x",&e)!=1);
  stkf(&stk);
  stk=stkn(b,e);
}

void menu() {

  bool quit=false;
  int choice;

  while(!quit) {
  
    printf(
      "--- Menu ---\n"
      "0. exit\n"
      "1. pushb\n"
      "2. popb\n"
      "3. dump mem\n"
      "4. new stack\n"
      "5. realloc mem\n\n"
      "choice: "    
    );

    scanf("%d",&choice);

    switch(choice) {
      case 0: quit=true; break;
      case 1: do_pushb(); break;
      case 2: do_popb(); break;
      case 3: dump(); break;
      case 4: do_new_stack(); break;
      case 5: do_realloc(); break;
      default:
        printf("invalid choice\n");      
    }  
  }
}



int main() {

  uint8_t v;

  srand(time(NULL));

  m=malloc(sizeof(*m)*mx);
  stk=stkn(0x0000,mx-1);

  menu();
  
  stkf(&stk);

  return 0;
}


