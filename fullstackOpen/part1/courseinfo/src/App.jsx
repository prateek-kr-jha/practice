import { useState } from "react";

const History = (props) => {
  if (props.allClicks.length == 0) {
    return <div>the app is used by pressing the buttons</div>;
  }

  return <div>button press history: {props.allClicks.join(" ")}</div>;
};

const Button = ({ onClick, text }) => <button onClick={onClick}>{text}</button>;

const App = () => {
  const [leftClick, setLeftClick] = useState(0);
  const [rightClick, setRightClick] = useState(0);
  const [allClicks, setAllClicks] = useState([]);
  const [total, setTotal] = useState(0);

  const handleLeftClick = () => {
    setAllClicks(allClicks.concat("L"));
    const updatedLeft = leftClick + 1;
    setLeftClick(updatedLeft);
    setTotal(updatedLeft + rightClick);
  };

  const handleRightClick = () => {
    setAllClicks(allClicks.concat("R"));
    const updatedRight = rightClick + 1;
    setRightClick(updatedRight);
    setTotal(leftClick + updatedRight);
  };

  return (
    <div>
      {leftClick}
      <Button onClick={handleLeftClick} text={"left"} />
      <Button onClick={handleRightClick} text={"right"} />
      {rightClick}
      <History allClicks={allClicks} />
    </div>
  );
};
export default App;
