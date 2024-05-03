const prisma = require("../config/prisma");
const { hashPassword } = require("../utils/bcrypt");
class UsersController {

  async getMyProfile(req, res) {
    const user = req.user;
    return res.status(200).send(user);
}

  async index(req, res) {
    try {
      const users = await prisma.user.findMany();
      return res.status(200).send(users);
    } catch (e) {
      return res.status(500).send({ message: e.message });
    }
  }

  async store(req, res) {
    try {
      const body = req.body;
      const user = await prisma.user.create({
        data: {
          name: body.name,
          email: body.email,
          password: await hashPassword(body.password),
        }
      });
      return res.status(201).send(user);
    } catch (e) {
      return res.status(500).send({ message: e.message });
    }
  }

  async show(req, res) {
    try {
      const id = req.params.id;
      const user = await prisma.user.findUnique({
        where: { id: parseInt(id) },
      });
      if(user==null) {
        return res.status(404).send({ message: "User not found" });
      }
      return res.status(200).send(user);
    } catch (e) {
      return res.status(500).send({ message: e.message });
    }
  }

  async update(req, res) {
    try {
      const id = req.params.id;
      const body = req.body;
      const user = await prisma.user.update({
        where: { id: parseInt(id) },
        data: body,
      });
      if (user === undefined) {
        return res.status(404).send({ message: "User not found" });
      }
      return res.status(200).send(user);
    } catch (e) {
      return res.status(500).send({ message: e.message });
    }
  }

  async destroy(req, res) {
    try {
      const id = req.params.id;
      const user = await prisma.user.delete({
        where: { id: parseInt(id) },
      });
      return res.status(200).send(user);
    } catch (e) {
      return res.status(500).send({ message: e.message });
    }
  }
}

module.exports = new UsersController();
