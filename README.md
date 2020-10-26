# product-revenue-calc
Calculates the approximate revenues for a product and its variations given market research.

## About
I was given the ["Green Ox" marketing case study](https://store.hbr.org/product/green-ox/UV0787) (made by the Darden School of Business) for my mid-term exam, and wanted to swiftly calculate a few things to support my stances, so I made this.
- Calculates revenues generated for each price point and determines the most optimal price. 
- Calculates revenues generated for each variety of the product (flavour) based on the most optimal price.

## Calculations
<img src="https://latex.codecogs.com/gif.latex?\inline&space;flavourRevenue\&space;=\&space;\left(\left(\left(\frac{%\&space;ofConsumerDemand\cdot&space;\frac{%ofFlavourDemand}{100}}{100}\right)&space;estimatedTotaDemand\right)optimalPrice\left(104\right)\right)" title="flavourRevenue\ =\ \left(\left(\left(\frac{%\ ofConsumerDemand\cdot \frac{%ofFlavourDemand}{100}}{100}\right) estimatedTotaDemand\right)optimalPrice\left(104\right)\right)" />

<img src="https://latex.codecogs.com/gif.latex?\inline&space;priceRevenue&space;=&space;(((\frac{%ofConsumerDemand}{100})%&space;ofTotalEstimatedDemand)price(104))" title="priceRevenue = (((\frac{%ofConsumerDemand}{100})% ofTotalEstimatedDemand)price(104))" />

