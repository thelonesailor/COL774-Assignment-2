# unset key

set key top left
set logscale x 10
set ylabel 'Accuracy %'
set xlabel 'C'
set grid
set term png
set output 'accuracy.png'
set datafile separator ","
plot 'output_d.csv' using 1:2 with linespoints title "Cross Validation Accuracy",'output_d.csv' using 1:3 with linespoints title "Test Accuracy"
