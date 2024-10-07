#include <stdio.h>

double fahrenheit(int celcius) {
  return (celcius * 9.0/5) + 32;
}

int kelvin(int celcius) {
  return celcius + 273;
}

int main() {

printf("%3.2f \n", fahrenheit(37));
printf("%i \n", kelvin(37));

}
