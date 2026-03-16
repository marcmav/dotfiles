-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")

vim.keymap.set("i", "jj", "<Esc>", { noremap = true })

-- open neotree with space + e
vim.keymap.set("n", "<leader>e", ":Neotree toggle<CR>")

-- ctrl + key arrows to change focus between windows (splits)
vim.keymap.set("n", "<C-h>", "<C-w>h") -- ctrl + h = left window focus
vim.keymap.set("n", "<C-j>", "<C-w>j") -- ctrl + j = down window focus
vim.keymap.set("n", "<C-k>", "<C-w>k") -- ctrl + k = up window focus
vim.keymap.set("n", "<C-l>", "<C-w>l") -- ctrl + l = left window focus

-- refactor
vim.keymap.set("n", "B", "^") -- "^" to B
vim.keymap.set("n", "E", "$") -- "$" to E

-- space  + tn (tabnew) and space + tc (tabclose)
vim.keymap.set("n", "<leader>tn", ":tabnew<CR>") -- space + tn == tabnew
vim.keymap.set("n", "<leader>c", ":tabclose<CR>") -- space + tc == tabclose

-- open terminal with space + t
vim.keymap.set("n", "<leader>t", ":terminal<CR>")
