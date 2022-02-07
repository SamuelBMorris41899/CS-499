import "./SectionIcon.css";

function SectionIcon(props) {
  return (
      <div className="sectionIcon">
        <img className="sectionIcon_Img" src={props.img} alt={props.name}/>
        <div className="sectionIcon_Name">
            <h3>{props.name}</h3>
        </div>
      </div>
  );
}

export default SectionIcon;
