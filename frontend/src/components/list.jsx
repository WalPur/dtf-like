import ArticleListElement from "./article";
import React, { useState, useEffect } from "react";

function ArticleList() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8000/articles/");
        const result = await response.json();
        setData(result);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching data:", error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);
  return (
    <div className="flex flex-col gap-5">
      {loading ? (
        <p>Загружается...</p>
      ) : (
        <>
          {data.results.map((item) => (
            <ArticleListElement data={item} />
          ))}
        </>
      )}
    </div>
  );
}

export default ArticleList;
