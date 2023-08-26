#include <stdio.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

typedef struct Stack Stack;

struct Stack {
  uint16_t size;
  uint16_t begin;
  uint16_t end;
  uint16_t top;
};


Stack *Stack_New(uint16_t begin,uint16_t end) {
  Stack *stack=malloc(sizeof(*stack));
  if(stack) {
    stack->begin=begin;
    stack->end=end;
    stack->top=stack->end;
    stack->size=(stack->end>=stack->begin?stack->end-stack->begin:stack->begin-stack->end)+1;
  }
  return stack;
}

void Stack_Free(Stack **stack) {
  free(*stack);
  *stack=NULL;
}

int pushb(Stack *stack,uint8_t value,uint8_t *mem,uint16_t mem_max) {
  printf("pushb %02X\n",value);
  if(stack->top==stack->begin) {
    printf("stack overflow\n");
    return 1;
  }
  if(stack->top==0) stack->top=mem_max; else stack->top--;
  mem[stack->top]=value;
  return 0;
}

int popb(Stack *stack,uint8_t *value,uint8_t *mem,uint16_t mem_max) {
  if (stack->top==stack->end) {
    printf("stack underflow\n");
    return 1;
  }
  *value=mem[stack->top];
  printf("popb %02X\n",*value);
  if(stack->top==mem_max) stack->top=0; else stack->top++;
  return 0;
}

void dump(Stack *stack,uint8_t *mem,uint16_t mem_max) {
  unsigned int i=0;
  int j=0;
  char str[18];
  char ch='\0';
  str[0]='\0';

  printf("\n");
  printf("\x1b[37;40m");
  while(i<=(unsigned int)mem_max) {
    if(i!=0 && i%16==0) printf("\n");
    if(i%16==0) printf("\x1b[1;37;40m%04X ",i);
    if(i%8==0) printf("\x1b[1;37;40m  ");

    if(i==stack->top)
      printf("\x1b[31;47m%02X",mem[i]);
    else if(stack->begin>stack->end && i<=stack->end)
      printf("\x1b[37;45m%02X",mem[i]);
    else if(stack->begin>stack->end && i>=stack->begin)
      printf("\x1b[37;45m%02X",mem[i]);
    else if(i>=stack->begin && i<=stack->end)
      printf("\x1b[37;45m%02X",mem[i]);
    else
      printf("\x1b[37;40m%02X",mem[i]);

    printf(" ");
 
    ch=mem[i];
    if(!isalnum(ch) && !ispunct(ch)) ch='.';
    
    str[j++]=ch;
    if(j==8) str[j++]=' ';
    str[j]='\0';

    if(j==17) {
      printf("\x1b[37;40m  %s",str);
      str[0]='\0';
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
  printf("\x1b[1;37;40m");
  if(j) printf("\x1b[37;40m  %s",str);
  printf("\n");
  printf("\x1b[0m");
  printf("\n");
}

void do_pushb(Stack *stack,uint8_t *mem,uint16_t mem_max) {
  unsigned int b;
  do {
    fflush(stdin);
    printf("Enter hex byte (00-FF): ");
  } while(scanf("%x",&b)!=1 || b>0xFF);
  pushb(stack,b%256,mem,mem_max);
}

void do_popb(Stack *stack,uint8_t *mem,uint16_t mem_max) {
  uint8_t value;
  popb(stack,&value,mem,mem_max);
}

void do_new_stack(Stack **stack,uint16_t mem_max) {
  unsigned int begin;
  unsigned int end;
  do {
    fflush(stdin);
    printf("Enter hex byte begin (0000-%04X): ",mem_max);
  } while(scanf("%x",&begin)!=1 || begin>(unsigned int)mem_max);
  do {
    fflush(stdin);
    printf("Enter hex byte end   (0000-%04X): ",mem_max);
  } while(scanf("%x",&end)!=1 || end>(unsigned int)mem_max);
  Stack_Free(stack);
  *stack=Stack_New(begin,end);
}

void do_realloc(Stack **stack,uint8_t **mem,uint16_t *mem_max) {
  unsigned int w;
  do {
    fflush(stdin);
    printf("Enter hex byte mem size (0000-FFFF): ");
  } while(scanf("%x",&w)!=1 || w>0xFFFF);
  *mem_max=w;
  *mem=realloc(*mem,sizeof(**mem)*(w+1));
  do_new_stack(stack,*mem_max);
}

void menu(Stack **stack,uint8_t **mem,uint16_t *mem_max) {

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
    fflush(stdin);

    switch(choice) {
      case 0: quit=true; break;
      case 1: do_pushb(*stack,*mem,*mem_max); break;
      case 2: do_popb(*stack,*mem,*mem_max); break;
      case 3: dump(*stack,*mem,*mem_max); break;
      case 4: do_new_stack(stack,*mem_max); break;
      case 5: do_realloc(stack,mem,mem_max); break;
      default:
        printf("invalid choice\n");      
    }  
  }
}



int main() {
  uint16_t mem_max=159;
  uint8_t *mem=malloc(sizeof(*mem)*mem_max);
  Stack *stack=NULL;

  srand(time(NULL));

  setbuf(stdout,_IOFBF);

  stack=Stack_New(0x0000,mem_max);

  menu(&stack,&mem,&mem_max);
  
  Stack_Free(&stack);

  return 0;
}


