# upgraded-landed-calc
creating a better landed cost evaluator

Plain English objectives:
This calculator is designed to determine the landed US customs costs for a product given its value, including duty, merchandise processing fee (MPF) and harbor maintenance fee (HMF). Eventually this will include the ability to select from a range of products (to determine the specific duty rate).

Duty:
Duty is calculated (for our purposes) as an ad valorem percentage of the value. For example, auto parts are (generally) dutiable at 2.5%.

Merchandise processing fee (MPF):
MPF is a bounded ad valorem percentage of the entered value. The minimum payable amount is $25, the maximum payable amount is $485, and otherwise it is .3464% of the value of the shipment.

in psuedocode:
MPF = 
IF('cost' x .003464<25, 25)
IF('cost' x .003464>485, 485)
ELSE 'cost' x .003464

Harbor maintenance fee (HMF):
HMF is a fee charged at .125% of the value of the shipment, but is only charged on ocean shipments.
