import { createContext, useContext, useState } from 'react';

const defaultProviderValues = {};

const AppContext = createContext(defaultProviderValues);

export const AppProvider = ({ children }) => {
  //   const [currentUser, setCurrentUser] = useState("");
  const [data, setData] = useState({ flipkart: [], ebay: [], indiamart: [] });
  const [dataBlog, setDataBlog] = useState([]);

  return (
    <AppContext.Provider
      value={{
        data,
        setData,
        dataBlog,
        setDataBlog,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => useContext(AppContext);
