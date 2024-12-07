function Author({ author, date }) {
  return (
    <div className="flex flex-col">
      <span>{author}</span>
      <span>{date}</span>
    </div>
  );
}

export default Author;
