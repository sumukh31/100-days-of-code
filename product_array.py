{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.\n",
    "\n",
    "# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "def prod_all(arr):\n",
    "\n",
    "    new_arr = [0] * len(arr)\n",
    "    product = 1\n",
    "    for num in arr:\n",
    "        product *= num\n",
    "    \n",
    "    for idx in range(len(arr)):\n",
    "        print (idx)\n",
    "        new_arr[idx] = int(product/arr[idx])\n",
    "    \n",
    "    return new_arr"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Without using division"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "def prod_array(arr):\n",
    "    \n",
    "    arr_len = len(arr)\n",
    "    \n",
    "    left = [0]*arr_len\n",
    "    right = [0]*arr_len\n",
    "    prod = [0]*arr_len\n",
    "    \n",
    "    left[0] = 1\n",
    "    right[-1] = 1\n",
    "    \n",
    "    for i in range(1,arr_len):\n",
    "        left[i] = arr[i-1] * left[i-1]\n",
    "    \n",
    "    for j in range(arr_len-2,-1,-1):\n",
    "        right[j] = arr[j+1]*right[j+1]\n",
    "    \n",
    "    for i in range(arr_len):\n",
    "        prod[i] = left[i] * right[i]\n",
    "    \n",
    "    return prod\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[120, 60, 40, 30, 24]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prod_array([1,2,3,4,5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Time Complexity O(n)\n",
    "# Space Complexity O(n)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Implement with time complexity O(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    " def prod_array_optimize(arr):\n",
    "        \n",
    "        arr_len = len(arr)\n",
    "        output = [1]*arr_len\n",
    "        \n",
    "        prod = 1\n",
    "        for i in range(arr_len):\n",
    "            output[i] *= prod\n",
    "            prod *= arr[i]\n",
    "\n",
    "        prod = 1\n",
    "        for i in range(arr_len-1,-1,-1):\n",
    "            output[i] *= prod\n",
    "            prod *= arr[i]\n",
    "        \n",
    "        return output\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[24, 12, 8, 6]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prod_array_optimize([1,2,3,4])"
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
