import TopNav from "./TopNav";
import SectionIcon from "./SectionIcon";
import "./LandingPage.css";

function LandingPage() {
  return (
    <div>
        <TopNav />
        <input class="search" type="text" placeholder="Search.."/>
        <button type="submit">Submit</button>
        <body>
            <div className="grid">
                <SectionIcon img="./img/sec1.1_Icon.png" name="Section 1.1"/>
                <SectionIcon img="./img/sec1.2_Icon.png" name="Section 1.2"/>
            </div>
        </body>
    </div>
  );
}

export default LandingPage;
