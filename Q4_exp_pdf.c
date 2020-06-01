#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
int i, n=10000;
float arr[n]; 

for (i=0;i<n;i++) 
{
float x=(1+rand()%1001)/1001.0;
arr[i]=-2*log(x); 
} 

FILE*fp=NULL;
fp=fopen("data.txt","w");
for (i=0;i<n;i++)
{
fprintf(fp,"%f\n",arr[i]);
}

/*then in linux terminal type, (gnuplot must be installed).
gcc Q4_exp_pdf.c -lm
./a.out
gnuplot
stats 'data.txt' using 1 nooutput
min=STATS_min
max=STATS_max
n_bin=10
bin_width=(max-min)/n_bin
bin(x)=bin_width*floor(x/bin_width)
set style fill solid
plot "data.txt" using (bin($1)):(1.0) smooth fnormal w boxes lc rgb "cyan" notitle,exp(-x/2)/2 title "exponential pdf." with lines lc rgb "dark-violet"
set xlabel "random numbers."
set ylabel "density."
set title "10000 exponential deviates using c code ."
replot
*/ 

}
