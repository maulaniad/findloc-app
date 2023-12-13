import { useState } from "react";
import { Link, router } from "@inertiajs/react";

const Register = (props) => {
  const [form, setForm] = useState({
    username: "",
    fullname: "",
    email: "",
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

    router.post("/register/", form);
  }

  return (
    <div className="w-52">
      <form onSubmit={submitHandler}>
        <input
          type="text"
          id="username"
          value={form.username}
          placeholder="Username"
          onChange={changeHandler}
          className="bg-gray-200 border-2 rounded focus:border-purple-500"
        />
        <input
          type="text"
          id="email"
          value={form.email}
          placeholder="Email"
          onChange={changeHandler}
          className="bg-gray-200 border-2 rounded focus:border-purple-500"
        />
        <input
          type="text"
          id="fullname"
          value={form.fullname}
          placeholder="Fullname"
          onChange={changeHandler}
          className="bg-gray-200 border-2 rounded focus:border-purple-500"
        />
        <input
          type="password"
          id="password"
          value={form.password}
          placeholder="Password"
          onChange={changeHandler}
          className="bg-gray-200 border-2 rounded focus:border-purple-500"
        />
        <button type="submit" className="min-w-fit bg-sky-400 px-4 rounded">
          Submit
        </button>
        <Link href="/login/">Login</Link>
      </form>
    </div>
  );
};

export default Register;
