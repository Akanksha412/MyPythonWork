{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the terms 5\n",
      "Fibonacci sequence:\n",
      "0 1 1 2 3 "
     ]
    }
   ],
   "source": [
    "terms = int(input(\"Enter the terms \"))  \n",
    "# first two intial terms  \n",
    "a = 0  \n",
    "b = 1  \n",
    "count = 0  \n",
    "  \n",
    "# check if the number of terms is Zero or negative  \n",
    "if (terms <= 0):\n",
    "    print(\"Please enter a valid integer\")  \n",
    "elif (terms == 1):  \n",
    "    print(\"Fibonacci sequence upto\",\":\")  \n",
    "    print(a)  \n",
    "else:  \n",
    "    print(\"Fibonacci sequence:\")  \n",
    "    while (count < terms) :  \n",
    "        print(a, end = ' ')  \n",
    "        c = a + b  \n",
    "       # updateing values  \n",
    "        a = b  \n",
    "        b = c\n",
    "        count=count + 1 \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
