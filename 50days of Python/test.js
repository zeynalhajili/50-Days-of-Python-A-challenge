console.log("Hello Vahid")
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer ZjdhMGFjMzItZjM2Ni00NWU0LThhMzAtNmE1ZmIyNTc2OGIwNDlhZTU2MGMtMzk3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYjE3NzI3YjAtNWNjZC0xMWVjLWJmNWEtNDk4MjdjYTUyNmMw", requestOptions)
  .then(response => response.json())
    .then(result => {
        
      console.log(result.items)
        
  })