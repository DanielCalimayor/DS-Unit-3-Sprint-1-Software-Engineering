{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-6-d523d4d86baa>, line 44)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-6-d523d4d86baa>\"\u001b[0;36m, line \u001b[0;32m44\u001b[0m\n\u001b[0;31m    else:\u001b[0m\n\u001b[0m       ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "from random import choice, randint, uniform\n",
    "from acme import Product\n",
    "\n",
    "\n",
    "def generate_products(quantity=30):\n",
    "    products = []\n",
    "    adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']\n",
    "    noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']\n",
    "\n",
    "    for _ in range(quantity):\n",
    "        name = (choice(adjective) + ' ' + choice(noun))\n",
    "        price = randint(5, 100)\n",
    "        weight = randint(5, 100)\n",
    "        flammability = uniform(0, 2.5)\n",
    "        products.append(Product(name=name, price=price,\n",
    "                                weight=weight, flammability=flammability))\n",
    "\n",
    "    return products\n",
    "\n",
    "\n",
    "def inventory_report(products):\n",
    "    unique_names = []\n",
    "    total_price = 0\n",
    "    total_weight = 0\n",
    "    total_flammability = 0\n",
    "    product_count = len(products)\n",
    "\n",
    "    for product in products:\n",
    "        unique_names.append(product.name)\n",
    "        total_price += product.price\n",
    "        total_weight += product.weight\n",
    "        total_flammability += product.flammability\n",
    "\n",
    "    print('ACME CORPORATION OFFICIAL INVENTORY REPORT \\n')\n",
    "    print('Unique product names:', len(set(unique_names)))\n",
    "    print('Average price:', (total_price/product_count))\n",
    "    print('Average weight:', (total_weight/product_count))\n",
    "    print('Average flammability:', (total_flammability/product_count))\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    inventory_report(generate_products())\n",
    "    \n",
    "    else:\n",
    "        print('FAILED')"
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
