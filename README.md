# Receipts For Lovely Loveseats
Practice Project #2 for fundamental Python

## Description
We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.


## Step to progress
1. Let’s add in our first item, the Lovely Loveseat that is the store’s namesake. Create a variable called **lovely_loveseat_description** and assign to it the following string:
> Lovely Loveseat. Tufted polyester blend on wood. 2 inches high x 40 inches wide x 30 inches deep. Red or white.

2. Create a price for the loveseat. Create a variable **lovely_loveseat_price** and set it equal to _254.00_.
3. Let’s extend our inventory with another characteristic piece of furniture! Create a variable called stylish_settee_description and assign to it the following string:
> Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.

4. Now let’s set the price for our Stylish Settee. Create a variable **stylish_settee_price** and assign it the value of _180.50_.
6. Fantastic, we just need one more item before we’re ready for business. Create a new variable called **luxurious_lamp_description** and assign it the following:
> Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.

8. Let’s set the price for this item. Create a variable called **luxurious_lamp_price** and set it equal to _52.15_.
9. In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well. Define the variable **sales_tax** and set it equal to _.088_. That’s 8.8%.
10. Our first customer is making their purchase! Let’s keep a running tally of their expenses by defining a variable called **customer_one_total**. Since they haven’t purchased anything yet, let’s set that variable equal to _0_ for now.
11. We should also keep a list of the descriptions of things they’re purchasing. Create a variable called **customer_one_itemization** and set that equal to the empty string _""_. We’ll tack on the descriptions to this as they make their purchases.
12. Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to **customer_one_total**.
13. Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to **customer_one_itemization**.
14. Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.
15. Let’s keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization.
16. They’re ready to check out! Let’s begin by calculating sales tax. Create a variable called **customer_one_tax** and set it equal to **_customer_one_total_** times **_sales_tax_**.
17. Add the sales tax to the customer’s total cost.
18. Let’s start printing up their receipt! Begin by printing out the heading for their itemization. Print the phrase _"Customer One Items:"_.
19. Print **customer_one_itemization**.
20. Now add a heading for their total cost: Print out _"Customer One Total:"_
21. Now print out their total! Our first customer now has a receipt for the things they purchased.
22. Congratulations! We created our catalog and served our first customer. We used our knowledge of strings and numbers to create and update variables. We were able to print out an itemized list and a total cost for our customer. Lovely!
