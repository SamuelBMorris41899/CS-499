import './TopNav.css';

function TopNav() {
  return (
    <div>
        <h1 class="header">CS 214 DISCRETE MATH WEB-CALCULATOR</h1>
        <div class="topnav">
          <a class="active" href={"#home"}>Home</a>
          <a href={"#sections"}>Sections</a>
        </div>
    </div>
  );
}

export default TopNav;
