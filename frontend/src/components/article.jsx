import Author from "./author";

function ArticleListElement({ data }) {
  return (
    <div className="w-[650px] h-[450px] bg-white rounded-md p-5">
      <Author author={data.author.username} date={data.date_created} />
      <img src={data.preview} alt="" />
      <div>{data.content}</div>
    </div>
  );
}
export default ArticleListElement;
