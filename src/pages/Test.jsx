import { Link, router } from "@inertiajs/react";


const Test = ({test}) => {
  return (
    <div>
      <h1>TEST</h1>
      <h1>{test.first_name}</h1>
      <h1>{test.last_name}</h1>
      <Link href="/">Balik ke Home</Link>
    </div>
  )
}

export default Test;
