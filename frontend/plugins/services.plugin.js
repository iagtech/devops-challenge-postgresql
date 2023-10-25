import { EnumService } from './enum.service'
import { TodoService } from './todo.service'


export default ({ app: { $axios } }, inject) => {
  const enumService = new EnumService($axios);
  const todoService = new TodoService($axios);

  inject('enumService', enumService);
  inject('todoService', todoService);
}
