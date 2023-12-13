import { useState } from "react";
import { Link, router } from "@inertiajs/react";

const Login = (props) => {
  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const changeHandler = (event) => {
    const key = event.target.id;
    const value = event.target.value;

    setForm((values) => ({
      ...values,
      [key]: value
    }));
  };

  const submitHandler = (event) => {
    event.preventDefault();

    router.post("/login/", form);
  }

  return (
    <div className="w-52">
      <form onSubmit={submitHandler}>
        <input
          type="text"
          id="username"
          placeholder="Username or Email"
          onChange={changeHandler}
          className="bg-gray-200 border-2 rounded w-full focus:border-purple-500"
        />
        <input
          type="password"
          id="password"
          placeholder="Password"
          onChange={changeHandler}
          className="bg-gray-200 border-2 rounded w-full focus:border-purple-500"
        />
        <input
          type="submit"
          value="Login"
          className="min-w-fit bg-sky-400 px-4 rounded"
        />
      </form>
      <Link href="/register/">Register</Link>
    </div>
  );
};

export default Login;
