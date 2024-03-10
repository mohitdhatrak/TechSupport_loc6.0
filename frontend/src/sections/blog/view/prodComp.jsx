import { useEffect } from 'react';
import './prodComp.css';
import { useApp } from 'src/context/app-context';

const cardsData1 = [
  {
    id: 1,
    type: 'free',
    title: 'Free Plan',
    description: 'Lorem ipsum',
    price: 19.99,
    recurrency: 14.99,
    mostPopular: false,
    data: ['2TB Storage', '100 E-mails'],
  },
  {
    id: 2,
    type: 'basic',
    title: 'Basic Plan',
    description: 'Lorem ipsum',
    price: 29.99,
    recurrency: 24.99,
    mostPopular: false,
    data: ['2TB Storage', '200 E-mails', '10 Accounts'],
  },
  {
    id: 3,
    type: 'medium',
    title: 'Medium Plan',
    description: 'Lorem ipsum',
    price: 69.99,
    recurrency: 59.99,
    mostPopular: false,
    data: ['10TB Storage', '500 E-mails', '20 Accounts'],
  },
];
// ---------------------------------
function CardDescription({ source, product_category }) {
  return (
    <div className="card-description">
      <h2>{source}</h2>
      <p>{product_category}</p>
    </div>
  );
}

function CardBilling({ price, reviews_count }) {
  return (
    <div className="card-billing">
      <p>
        <strong className="price">₹ {price}</strong>
        {/* <strong> / mo.</strong> */}
      </p>
      <p>
        <span className="recurrency">Reviews Count: {reviews_count}/monthly</span>
      </p>
    </div>
  );
}

function CardFeatures({ description }) {
  return (
    <div className="card-features">
      <ul>
        {description?.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

function openURL(url) {
  window.open(url, '_blank');
}

function CardAction({ url }) {
  return (
    <div className="card-action">
      <button onClick={(url) => openURL(url)}>CHECK</button>
    </div>
  );
}

function PricingCard(props) {
  const { source, reviews_count, title, description, price, image_url, product_category, url } =
    props.data;

  return (
    <div className={`card pricing-card ${source}`}>
      <CardDescription source={source} product_category={product_category} />
      <CardBilling price={price} reviews_count={reviews_count} />
      <CardFeatures description={description} />
      <CardAction url={url} />
    </div>
  );
}

export default function ProdComp() {
  const { data } = useApp();

  const cardsData = [];

  if (data?.flipkart?.length > 0) {
    cardsData.push(data?.flipkart[0]);
  }
  if (data?.ebay?.length > 0) {
    cardsData.push(data?.ebay[0]);
  }
  if (data?.indiamart?.length > 0) {
    cardsData.push(data?.indiamart[0]);
  }

  function handleClick() {
    console.log('Button clicked!');
  }

  return (
    <>
      {cardsData.length > 0 ? (
        <div className="prod-wrapper">
          {cardsData?.map((props, index) => {
            return <PricingCard data={props} key={index} clickMe={handleClick} />;
          })}
        </div>
      ) : (
        <></>
      )}
      {cardsData.length > 0 ? (
        <></>
      ) : (
        <>
          <div className="skeleton-prod-wrapper">
            {cardsData1.map((props) => {
              return (
                <div className="cardS pricing-card" key={props.id} id="outerCard">
                  <div className="skeleton-card">
                    <div className="skeleton-description">
                      <h2>&nbsp;</h2>
                      <p>&nbsp;</p>
                    </div>
                    <div className="skeleton-billing">
                      <p>
                        <strong className="price">&nbsp;</strong>
                        <strong id="NA"> Not available</strong>
                      </p>
                      <p>
                        <span className="recurrency">&nbsp;</span>
                      </p>
                    </div>
                    <div className="skeleton-features">
                      <ul>
                        <li>&nbsp;</li>
                        <li>&nbsp;</li>
                        <li>&nbsp;</li>
                      </ul>
                    </div>
                    <div className="skeleton-action">
                      <button disabled>B U Y</button>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </>
      )}

      {/* <BarChart
        xAxis={[{ scaleType: 'band', data: ['group A', 'group B', 'group C'] }]}
        series={[{ data: [4, 3, 5] }, { data: [1, 6, 3] }, { data: [2, 5, 6] }]}
        width={500}
        height={300}
      /> */}
    </>
  );
}
