"use scrict";


 

class Drone {
  constructor(name, x, y, z) {
    this.name = name;
    this.x = x;
    this.y = y;
    this.z = z;
    this.waypoints = []
  }

  async init() {
    console.log(this.name, "Ready");
    await this.takeOff();
  }

  async takeOff() {
    console.log(this.name, "Taking off");
    await new Promise(resolve => setTimeout(resolve, 1000)); //sleep 
    console.log(this.name, "Airborne");
    return
  }

  takeWaypoints(givenWaypoints = []) {
    this.waypoints = [...this.waypoints, ...givenWaypoints];
  }

  async flyToWaypoints() {
    if (this.waypoints.length === 0) {
      console.log("No more waypoints");
      return;
    };
    const waypoint = this.waypoints.shift();
    console.log(this.name, "Flying to", waypoint);
    await new Promise(resolve => setTimeout(resolve, 5000)); //sleep 
    this.x = waypoint[0];
    this.y = waypoint[1];
    this.z = waypoint[2];
    console.log(this.name, "Got to ", this.x, this.y, this.z);
    this.flyToWaypoints()
  }

};









(async ()=>{
  const myDrone0 = new Drone("drone1", 0, 0, 0)
  myDrone0.takeWaypoints([[1, 1, 1], [2, 2, 2], [3, 3, 3]]);
  await myDrone0.init();
  myDrone0.flyToWaypoints()
  setTimeout(()=>{
    myDrone0.takeWaypoints([ [4, 4, 4]]);
  },1000);  

})();



