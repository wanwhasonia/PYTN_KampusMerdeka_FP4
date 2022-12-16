import pickle
import streamlit as st

model = pickle.load(open('clustering.pkl','rb'))

def main():
    st.title('Credit Card User Segmentation Prediction')

    #input variables
    BALANCE = st.text_input('Balance')
    BALANCE_FREQUENCY = st.text_input('Balance Frequency')
    PURCHASES = st.text_input('Purchases')
    ONEOFF_PURCHASES = st.text_input('One Off Purchases')
    INSTALLMENTS_PURCHASES = st.text_input('Installments Purchases')
    CASH_ADVANCE = st.text_input('Cash Advance')
    PURCHASES_FREQUENCY = st.text_input('Purchases Frequency (0-1)')
    ONEOFF_PURCHASES_FREQUENCY = st.text_input('One Off Purchases Frequency (0-1)')
    PURCHASES_INSTALLMENTS_FREQUENCY = st.text_input('Purchases Installments Frequency (0-1)')
    CASH_ADVANCE_FREQUENCY = st.text_input('Cash Advance Frequency')
    CASH_ADVANCE_TRX = st.text_input('Cash Advance Transaction')
    PURCHASES_TRX = st.text_input('Purchases Transaction')
    CREDIT_LIMIT = st.text_input('Credit Limit')
    PAYMENTS = st.text_input('Payments')
    MINIMUM_PAYMENTS = st.text_input('Minimum Payments')
    PRC_FULL_PAYMENT = st.text_input('Price Full Payment')
    TENURE = st.text_input('Tenure (6-12)')


    #result[0]ion code
    if st.button('Predict'):
        result = model.predict([[BALANCE, BALANCE_FREQUENCY, PURCHASES, ONEOFF_PURCHASES, 
                                        INSTALLMENTS_PURCHASES, CASH_ADVANCE, PURCHASES_FREQUENCY,
                                        ONEOFF_PURCHASES_FREQUENCY, PURCHASES_INSTALLMENTS_FREQUENCY, 
                                        CASH_ADVANCE_FREQUENCY, CASH_ADVANCE_TRX, PURCHASES_TRX, CREDIT_LIMIT, 
                                        PAYMENTS, MINIMUM_PAYMENTS, PRC_FULL_PAYMENT, TENURE]])
        st.write("This user belongs to cluster no: ", result[0])

        if result[0] == 0:
            st.write("Middle Ground Users")
        elif result[0] == 1:
            st.write('High Credit Frequent Purchaser Users')
        elif result[0] == 2:
            st.write('High Cash Advance Users')
        elif result[0] == 3:
            st.write('Frugal Credit Users')
        elif result[0] == 4:
            st.write('Very Frugal Credit Users')

if __name__=='__main__':
    main()
