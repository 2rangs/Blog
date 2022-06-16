import axios from "axios";
const url = "http://192.168.1.55";

export default{
    test: function (): any {
        return axios.get(url + "/test");
      },
}