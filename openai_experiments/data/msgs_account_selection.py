messages = [
    dict(
        role="system",
        content="""
            X is the customer of a Park National Bank. X holds the following accounts:
            
            A checking account with a balance of $23350.00. In the past three months of this year, this account was 
            used for 91 transactions, of which 18 were at foreign ATMs that carried a total fee of $11.15, 50 of which 
            used a debit card, the rest used bill pay.
            
            In 2022 this account was used for 24 transactions, 12 were using a debit card, 6 used bill pay, and 6 were 
            at Park National Bank ATMs. 
            
            In 2021 this account was used for 56 transactions, 44 used a debit card, 10 
            used bill pay, and 2 were at Park National Bank ATMs. 
            
            In 2020 this account was used for 122 transactions, 
            98 used a debit card, 20 used Park National Bank ATMs, 4 used foreign ATMs with total feed of $22.50.
            
            A savings account with a balance of $9950.00. This account had a balance of $8200.00 in January of 2022, 
            $7100.00 in January of 2021, and $6310.00 in January of 2020.
            
            The customer also has a mortgage with a balance of $150250.00 on a property valued at $275000.00. The 
            mortgage carries an APR of 4.8%.
            ---
            Park National Bank offers the following checking account products:
            
            1. Premium Account: 
                - fee: $10 per month
                - interest paid: 1% APR
                - foreign ATM fee credit: repays fees for up to 10 foreign ATM transactions
                - fee reductions: $10 reduction for customers who make 20 or more debit card transactions in a year, $5 reduction for customers who make 10-19 debit card transactions in a year.
            
            2. Standard Account: 
                - fee: $5 per month
                - interest paid: 0.2% APR
                - foreign ATM fee credit: none
                - fee reductions: $5 reduction for customers who use more than 10 debit card transactions in a year.
            
            3. Free Account: 
                - fee: $0 per month
                - interest paid: none
                - foreign ATM fee credit: none
                - fee reductions: none.
        """
    ),
    dict(
        role="system",
        content="""
            You are a banker advising a customer. Use numeric information about the number of debit card transactions 
            the customer uses to determine the fee for each account type and then select the best account type based on 
            the fees the customer would pay after any deductions for debit card usage, interest paid by the account, 
            and any foreign ATM fees that the customer is likely to incur that would be offset by the account.
        """
    ),
    dict(
        role="assistant",
        content="""
            Which of Park National Bank's checking account products would best suit customer X?
        """
    ),
]

